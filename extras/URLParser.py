"""
Write a sanitization script that prevents a user from inputting any type of URL manipulation.
For example | <script >' OR 1 = 1 </script>

Character	HTML Entity Note
&	&amp;	Interpreted as the beginning of an entity or character reference.
<	&lt;	Interpreted as the beginning of a tag
>	&gt;	Interpreted as the ending of a tag
"	&quot;	Interpreted as the beginning and end of an attribute's value.

Special characters needing encoding are: ':', '/', '?', '#', '[', ']', '@', '!', '$', '&', "'", '(', ')', '*', '+', ',', ';', '=',
as well as '%' itself. Other characters don't need to be encoded, though they could.

':'	'/'	'?'	'#'	'['	']'	'@'	'!'	'$'	'&'	"'"	'('	')'	'*'	'+'	','	';'	'='	'%'	' '
%3A	%2F	%3F	%23	%5B	%5D	%40	%21	%24	%26	%27	%28	%29	%2A	%2B	%2C	%3B	%3D	%25	%20 or +
"""
import re

# def tokenize(text):
    # print("--Text--\n", text, "\n")
#     no_punc_text = remove_punctuation(text)
#     sentences = split_by_sentence(no_punc_text)
#     start = add_start(sentences)
#     end = add_stop(start)
#     propper = end
#     # for line in propper:
#     # print(line)
#     tokens = split_on_whitespace(propper)
#     return tokens


# def split_by_sentence(text):
#     # print("--Split by line--")
#     sentences = re.split(r'\.(?:\s)+', text)
#     return sentences


def remove_punctuation(text):
    no_punc_text = re.sub('[,()]', '', text)
    no_punc_text = re.sub('--', ' ', no_punc_text)
    # print("--No Punctuation--\n", no_punc_text, "\n")
    return no_punc_text


def remove_html(text):
    no_and = re.sub('\&', '\&amp;', text)
    no_beginning_tag = re.sub('\<', '', no_and)
    no_ending_tag = re.sub('\>', '', no_beginning_tag)
    no_double_quote = re.sub('\"', '', no_ending_tag)
    return no_double_quote


def sanitize_sql(text):
    no_sql_attack = re.sub(
        '\' OR 1 = 1', '[BLOCKED] FOUND SQL ATTACK [BLOCKED]', text)
    return no_sql_attack


def sanitize_script(text):
    text = front_script(text)
    text = back_script(text)
    return text


def front_script(text):
    no_script_attack = re.sub(
        '<script>', '[BLOCKED] FOUND BEGINING SCRIPT ATTACK [BLOCKED]', text)
    return no_script_attack


def back_script(text):
    no_script_attack = re.sub(
        '</script>', '[BLOCKED] FOUND ENDING SCRIPT ATTACK [BLOCKED]', text)
    return no_script_attack


if __name__ == "__main__":
    attack_script = '<script> I am attacking </script>'
    attack_sql = '\' OR 1 = 1'
    print(sanitize_sql(attack_sql))
    print(sanitize_script(attack_script))
