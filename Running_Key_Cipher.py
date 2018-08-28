encode = input("Enter 1 for encoding or 0 for decoding\n")
if encode:
    txt = raw_input("Enter plain text to encode\n")
else:
    txt = raw_input("Enter cipher text to decode\n")
key = raw_input("Enter key\n")


def de_encode_word(txt, key, encode=1):
    ltrs = [
        None, 'a', 'b',
        'c', 'd', 'e', 'f', 'g', 'h',
        'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't',
        'u', 'v', 'w', 'x', 'y', 'z']

    output = ""
    for i, l in enumerate(txt):
        if l == " ":
            output += " "
        else:
            current = ""
            key_ltr = key[i % len(key)]
            key_ltr_num = ltrs.index(key_ltr)
            txt_ltr_num = ltrs.index(l)
            if encode:
                output_ltr_num = txt_ltr_num + key_ltr_num
                output_ltr = ltrs[
                    output_ltr_num - 26
                    if output_ltr_num > 26 else output_ltr_num]
            else:
                output_ltr_num = txt_ltr_num - key_ltr_num
                output_ltr = ltrs[
                    txt_ltr_num + 26 - key_ltr_num
                    if txt_ltr_num <= key_ltr_num else txt_ltr_num - key_ltr_num]

            output += output_ltr
            current += (
                "key ltr num: %s - %s\n"
                "Plain ltr num: %s - %s\n"
                "Output: %s - %s\n\n") % (
                key_ltr, key_ltr_num,
                l, txt_ltr_num,
                output_ltr, output_ltr_num)
    return output

output = ""
for word in txt.split(" "):
    output += de_encode_word(word, key, encode)
    output += " "
print output
