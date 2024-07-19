import os
import json
from google.cloud import translate
from icecream import ic

def translate_text(keys:list=["hello", "world"], text:list =["merhaba", "dünya"], project_id="black-outlet-402109", source="tr", target="en-US"):

    print("GOOGLE")
    print("Translating...")

    max_items_per_request = 500
    ic("keys: ", keys)
    ic("text: ", text)

    dict_to_return = {}

    request_count = len(keys) // max_items_per_request + 1

    client = translate.TranslationServiceClient()
    location = "global"
    parent = f"projects/{project_id}/locations/{location}"

    #divide into batches

    batches = []

    for i in range(request_count):
        batches.append(text[i*max_items_per_request:(i+1)*max_items_per_request])

    translations_array = []

    print("batches length: " + str(len(batches)))

    for i in range(len(batches)):
        print(f"batch{i}length: " + str(len(batches[i])))


    for batch in batches:
        print(f"for batch of length {str(len(batch))}")
        try:
            response = client.translate_text(
                request={
                    "parent": parent,
                    "contents": batch,
                    "mime_type": "text/plain",
                    "source_language_code": source,
                    "target_language_code": target,
                }
            )
            translations_output = []
            for translation in response.translations:
                translations_output.append(translation.translated_text)

            print("addin translations output of len " + str(len(translations_output)))

            print(f"trs array from:" + str(len(translations_array)))
            translations_array.extend(translations_output)
            print(f"trs array to:" + str(len(translations_array)))
        except Exception as e:
            print(e)
            print("error occured")
            return None

    print("keys length: " + str(len(keys)))
    print("translations array length: " + str(len(translations_array)))

    for i in range(len(keys)):
        dict_to_return[keys[i]] = translations_array[i]

    return dict_to_return


def create_reverse_dict(original_dict):
    reverse_dict = {}
    for key, value in original_dict.items():
        if value not in reverse_dict:
            reverse_dict[value] = key
        else:
            # Handle duplicate values, if needed
            pass
    return reverse_dict

def get_files(source_name, target_name, create_name, source_lang, target_lang):

    source_file = os.path.join(os.getcwd(), source_name)

    with open(source_file, "r",encoding='utf-8') as f:
        source_data:dict = json.load(f)

    for key, value in source_data.items():
        if value == "--" or value == "" or value == " " or value == None or value == "null" or value == "Null":
            source_data[key] = "NULL"

    target_data = translate_text(list(source_data.keys()), list(source_data.values()), "black-outlet-402109", source_lang, target_lang)

    #create new json file
    new_target_file = os.path.join(os.getcwd(), create_name)
    with open(new_target_file, "w", encoding='utf-8') as f:
        json.dump(target_data, f, ensure_ascii=False, indent=4)
    ic("new file created")

    return
    target_file = os.path.join(os.getcwd(), create_name)
    with open(target_file, "w", encoding='utf-8') as f:
        json.dump(target_data, f, ensure_ascii=False, indent=4)

    target_file = os.path.join(os.getcwd(), target_name)

    ic(source_file)
    ic(target_file)

    # load json files
    with open(source_file, "r",encoding='utf-8') as f:
        source_data:dict = json.load(f)
    with open(target_file, "r",encoding='utf-8') as f:
        target_data:dict = json.load(f)


    ic(source_data)
    ic(target_data)

    to_be_translated = {}

    for item in target_data.items():
        value = item[1]
        ic(value)
        if (not isinstance(value, str) or value == "" or value == " " or value == None or value == "null" or value == "Null"):
            ic("value is empty")
            value = "NULL"

        if value == "--":
            #find key from target_data
            key = item[0]
            ic("key is: ", key)
            ## get value from source_data
            source_value = source_data[key]

            if (not isinstance(source_value, str) or source_value == "" or source_value == " " or source_value == None or source_value == "null" or source_value == "Null"):
                ic("value is empty")
                source_value = "NULL"

            ic("source value is: ", source_value)
            ## add to to_be_translated dict

            to_be_translated[key] = source_value

            # ## translate source_value
            # print("Translating..." + source_value + " to " + target_lang)
            # translated_text = translate_text(source_value, "black-outlet-402109", source_lang, target_lang)
            # ic(translated_text)
            # ## add translated text to target_data
            # target_data[key] = translated_text



    ic("new data: ", target_data)

    #update target_data

    ic("to be translated: ", to_be_translated)

    new_dict:dict = translate_text(list(to_be_translated.keys()), list(to_be_translated.values()), "black-outlet-402109", source_lang, target_lang)

    ic("new dict: ", new_dict)

    for key, value in new_dict.items():
        target_data[key] = value

    #create new json file
    new_target_file = os.path.join(os.getcwd(), create_name)
    with open(new_target_file, "w", encoding='utf-8') as f:
        json.dump(target_data, f, ensure_ascii=False, indent=4)
    ic("new file created")

# get_files("tr.json", "en.json", "new_en.json", "tr", "en-US")
# get_files("new_en.json", "ar.json", "new_ar.json", "en-US", "ar")
# get_files("new_en.json", "zh-Hans.json", "new_zh-Hans.json", "en-US", "zh-Hans")
# get_files("new_en.json", "fr.json", "new_fr.json", "en-US", "fr")
# get_files("new_en.json", "de.json", "new_de.json", "en-US", "de")
# get_files("new_en.json", "es.json", "new_es.json", "en-US", "es")
# get_files("new_en.json", "ru.json", "new_ru.json", "en-US", "ru")
# get_files("new_en.json", "he.json", "new_he.json", "en-US", "he")

get_files("en.json", "", "tr.json", "en-US", "tr")
get_files("en.json", "", "ar.json", "en-US", "ar")
get_files("en.json", "", "zh.json", "en-US", "zh-Hans")
get_files("en.json", "", "fr.json", "en-US", "fr")
get_files("en.json", "", "de.json", "en-US", "de")
get_files("en.json", "", "es.json", "en-US", "es")
get_files("en.json", "", "ru.json", "en-US", "ru")
get_files("en.json", "", "he.json", "en-US", "he")