#1
import random
def get_words_from_file(file_path):
    with open(file_path,'r')as file:
        words=file.read().split()
    return words
def get_random_sentence(words,length):
    random_words=random.sample(words,length)
    sentence=''.join(random_words)
    return sentence.lower()
def main():
    print('Random Sentence Generator')
file_path='path/to/sowpods.txt'
words=get_words_from_file(file_path)

try:
    sentence_length=int(input('Enter the desired sentence length(beetween 2 and 20)'))
    if not 2<=sentence_length<=20:
        print('Error:Sentence length must be beetween 2 and 20')
except ValueError:
    print('Error:Please enter a valid integer for sentence length')
random_sentence=get_random_sentence(words,sentence_length)
print('Generated sentence:',random_sentence)                

if __name__=='main':
    main()



#2
import json


sample_dict = json.loads(sampleJson)

salary_value = sample_dict["company"]["employee"]["payable"]["salary"]
print("Salary:", salary_value)

sample_dict["company"]["employee"]["birth_date"] = "1990-01-01"  # Replace with the desired birth date

output_file_path = "output.json"  
with open(output_file_path, 'w') as output_file:
    json.dump(sample_dict, output_file, indent=2)

print(f"Updated JSON saved to: {output_file_path}")





















import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
#salary
salary_value=json.loads(sampleJson)["company"]["employee"][ "payable"][ "salary"]
print("Salary:",salary_value)
#birth_Date
data=json.loads(sampleJson)
data["company"]["employee"][ "birth_date"]="2002-08-04"
#Dictionnary
with open('output.json','w')as json_file:
    json.dump(data,json_file,indent=2)
print("JSON saved to'output.")