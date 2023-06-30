from transformers import LlamaTokenizerFast, LlamaForCausalLM
#import ray


class LlamaMonitor:
    def __init__(self):
        model_path = "/home/gridsan/omoll/LLaMa_7B_hf/"
        self.model = LlamaForCausalLM.from_pretrained(model_path)
        self.tokenizer = LlamaTokenizerFast.from_pretrained(model_path)

    def run_model(self, prompt, max_length):
        inputs = self.tokenizer(prompt, return_tensors='pt')
        generate_ids = self.model.generate(inputs.input_ids, max_length)
        output = self.tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
        return output