import numpy as np
import pickle

from tensorflow.keras.models import Model, load_model
from tensorflow.keras.layers import Input, LSTM, Dense


pickle_filename = "pickledInfo.pickle"
model_filename = "xorModel.h5"

with open("files/" + pickle_filename, "rb") as pickle_file:
    info = pickle.load(pickle_file)

input_token_index = info["input_token_index"]
target_token_index = info["target_token_index"]
num_encoder_tokens = info["num_encoder_tokens"]
num_decoder_tokens = info["num_decoder_tokens"]
max_encoder_seq_length = info["max_encoder_seq_length"]
max_decoder_seq_length = info["max_decoder_seq_length"]
latent_dim = info["latent_dim"]

reverse_input_char_index = dict((i, char) for char, i in input_token_index.items())
reverse_target_char_index = dict((i, char) for char, i in target_token_index.items())


model = load_model("files/" + model_filename)

encoder_inputs = model.input[0]
encoder_outputs, state_h_enc, state_c_enc = model.layers[2].output
encoder_states = [state_h_enc, state_c_enc]
encoder_model = Model(encoder_inputs, encoder_states)

decoder_inputs = model.input[1]
decoder_state_input_h = Input(shape=(latent_dim,), name='input_3')
decoder_state_input_c = Input(shape=(latent_dim,), name='input_4')
decoder_states_inputs = [decoder_state_input_h, decoder_state_input_c]
decoder_lstm = model.layers[3]
decoder_outputs, state_h_dec, state_c_dec = decoder_lstm(decoder_inputs, initial_state=decoder_states_inputs)
decoder_states = [state_h_dec, state_c_dec]
decoder_dense = model.layers[4]
decoder_outputs = decoder_dense(decoder_outputs)
decoder_model = Model([decoder_inputs] + decoder_states_inputs, [decoder_outputs] + decoder_states)


def decode_sequence(input_seq):
    states_value = encoder_model.predict(input_seq)

    target_seq = np.zeros((1, 1, num_decoder_tokens))
    target_seq[0, 0, target_token_index['\t']] = 1.

    stop_condition = False
    decoded_sentence = ''
    while not stop_condition:
        output_tokens, h, c = decoder_model.predict([target_seq] + states_value)

        sampled_token_index = np.argmax(output_tokens[0, -1, :])
        sampled_char = reverse_target_char_index[sampled_token_index]
        decoded_sentence += sampled_char

        if (sampled_char == '\n') or (len(decoded_sentence) > max_decoder_seq_length):
            stop_condition = True

        target_seq = np.zeros((1, 1, num_decoder_tokens))
        target_seq[0, 0, sampled_token_index] = 1.

        states_value = [h, c]

    return decoded_sentence


def process_text(input_text):
	encoder_input_data = np.zeros(
		(1, max_encoder_seq_length, num_encoder_tokens),
		dtype='float32')

	for t, char in enumerate(input_text):
		encoder_input_data[0, t, input_token_index[char]] = 1.
	encoder_input_data[0, t + 1:, input_token_index[' ']] = 1.

	return encoder_input_data
