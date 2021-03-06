import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration

context = "The Apollo program, also known as Project Apollo, was the third United States human spaceflight " \
          "program carried out by the National Aeronautics and Space Administration (NASA), which accomplished " \
          "landing the first humans on the Moon from 1969 to 1972. First conceived during Dwight D. " \
          "Eisenhower's administration as a three-man spacecraft to follow the one-man Project Mercury which " \
          "put the first Americans in space, Apollo was later dedicated to President John F. Kennedy's " \
          "national goal of landing a man on the Moon and returning him safely to the Earth by the end of the " \
          "1960s, which he proposed in a May 25, 1961, address to Congress. Project Mercury was followed by " \
          "the two-man Project Gemini. The first manned flight of Apollo was in 1968. Apollo ran from 1961 to " \
          "1972, and was supported by the two-man Gemini program which ran concurrently with it from 1962 to " \
          "1966. Gemini missions developed some of the space travel techniques that were necessary for the " \
          "success of the Apollo missions. Apollo used Saturn family rockets as launch vehicles. Apollo/Saturn " \
          "vehicles were also used for an Apollo Applications Program, which consisted of Skylab, " \
          "a space station that supported three manned missions in 1973-74, and the Apollo-Soyuz Test Project, " \
          "a joint Earth orbit mission with the Soviet Union in 1975. "

gpu = torch.device('cuda')
model = T5ForConditionalGeneration.from_pretrained('t5-large').to(gpu)
tokenizer = T5Tokenizer.from_pretrained('t5-large')
tokens_input = tokenizer.encode(text="summarize: " + context, return_tensors="pt", max_length=1024, truncation=True)
summary_ids = model.generate(tokens_input.to(gpu), min_length=60, max_length=180, length_penalty=4.0)
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

# the Apollo program, also known as Project Apollo, was the third human spaceflight program carried out by the
# national aeronautics and space administration. it was dedicated to president john f. kennedy's national goal of
# landing a man on the moon and returning him safely to the earth by the end of the 1960s. the first manned flight of
# Apollo was in 1968.
print(summary)
