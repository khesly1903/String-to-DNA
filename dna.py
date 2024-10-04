def string_to_dna(text):
    dna_parts = []
    for char in text:
        ascii_value = ord(char)
        binary_value = format(ascii_value, '08b')

        dna_part = ""
        for i in range(0, 8, 2):
            baz = binary_value[i:i+2]
            match baz:
                case "00":
                    dna_part += "A"
                case "01":
                    dna_part += "T"
                case "10":
                    dna_part += "C"
                case "11":
                    dna_part += "G"

        dna_parts.append(dna_part)

    dna = " ".join(dna_parts)
    return dna


def dna_to_string(dna):
    dna_parts = dna.split()

    text = ""
    for baz in dna_parts:
        binary_value = ""
        for nucleotide in baz:
            match nucleotide:
                case "A":
                    binary_value += "00"
                case "T":
                    binary_value += "01"
                case "C":
                    binary_value += "10"
                case "G":
                    binary_value += "11"

        ascii_value = int(binary_value, 2)
        char = chr(ascii_value)
        text += char

    return text

#sample usage
msg = "sample usage"

dna = string_to_dna(msg)
print(dna)
# TGAG TCAT TCGT TGAA TCGA TCTT ACAA TGTT TGAG TCAT TCTG TCTT

msg1 = dna_to_string(dna)
print(msg1)
