# TUGAS BESAR TEORI BAHASA DAN AUTOMATA
# IF-43-05
# KELOMPOK 1
#   Arpriansah Yonathan (1301194112)
#   Igga Febrian Virgiani (1301194283)
#   Manuel Benedict (1301194182)

# DESKRIPSI
#   Bahasa yang digunakan sebagai bahasa alami pada tugas ini adalah bahasa Inggris.
#   FA yang dibangun pada tugas ini adalah aturan grammar yang terdiri dari subject-verb-object dengan aturan present simple.
#   Aturan CFG :
#       <X> := <S><V><O>
#       <S> := maya | miko | moni
#       <V> := pays | peels | picks
#       <O> := banana | berry | book | blouse


#library
import string

#input example
sentence = 'lim ride bicycle'
input_string = sentence. lower () + '#'

#initialization
alphabet_list = list(string.ascii_lowercase)
state_list = ['q0', 'ql', 'q2', 'q3', 'q4','q5' , 'q6','q7', 'q8','q9','q10', 'q11','q12','q13','q14','q15','q16','q17','q18','q19','q20',
'q21','q22','q23','q24','q25','q26','q27','q28','q29','q30','q31','q32','q33','q34','q35','q36','q37','q38','q39','q40','q41']

transition_table = {}

for state in state_list:
    for alphabet in alphabet_list:
        transition_table[(state, alphabet)] = 'error'
    transition_table[(state,'#')] = 'error'
    transition_table[(state,' ')] = 'error'

#spaces before input string
transition_table ['q0' ,' '] = 'q0'

#update the transition table for the following token: maya
transition_table[('q0','m')] = 'q1'
transition_table[('q1','a')] = 'q2'
transition_table[('q2','y')] = 'q3'
transition_table[('q3','a')] = 'q4'
transition_table[('q4',' ')] = 'q11'
transition_table[('q4','#')] = 'accept'
transition_table[('q11',' ')] = 'q11'
transition_table[('q11','#')] = 'accept'

#update the transition table for the following token: miko
transition_table[('q0','m')] = 'q1'
transition_table[('q1','i')] = 'q5'
transition_table[('q5','k')] = 'q6'
transition_table[('q6','o')] = 'q7'
transition_table[('q7',' ')] = 'q11'
transition_table[('q7','#')] = 'accept'
transition_table[('q11',' ')] = 'q11'
transition_table[('q11','#')] = 'accept'

#update the transition table for the following token: moni
transition_table[('q0','m')] = 'q1'
transition_table[('q1','o')] = 'q8'
transition_table[('q8','n')] = 'q9'
transition_table[('q9','i')] = 'q10'
transition_table[('q10',' ')] = 'q11'
transition_table[('q10','#')] = 'accept'
transition_table[('q11',' ')] = 'q11'
transition_table[('q11','#')] = 'accept'

#update the transition table for the following token: pays
transition_table[('q11','p')] = 'q12'
transition_table[('q12','a')] = 'q13'
transition_table[('q13','y')] = 'q14'
transition_table[('q14','s')] = 'q21'
transition_table[('q21',' ')] = 'q22'
transition_table[('q21','#')] = 'accept'
transition_table[('q22',' ')] = 'q22'
transition_table[('q22','#')] = 'accept'

#update the transition table for the following token: peels
transition_table[('q11','p')] = 'q12'
transition_table[('q12','e')] = 'q15'
transition_table[('q15','e')] = 'q16'
transition_table[('q16','l')] = 'q17'
transition_table[('q17','s')] = 'q21'
transition_table[('q21',' ')] = 'q22'
transition_table[('q21','#')] = 'accept'
transition_table[('q22',' ')] = 'q22'
transition_table[('q22','#')] = 'accept'

#update the transition table for the following token: picks
transition_table[('q11','p')] = 'q12'
transition_table[('q12','i')] = 'q18'
transition_table[('q18','c')] = 'q19'
transition_table[('q19','k')] = 'q20'
transition_table[('q20','s')] = 'q21'
transition_table[('q21',' ')] = 'q22'
transition_table[('q21','#')] = 'accept'
transition_table[('q22',' ')] = 'q22'
transition_table[('q22','#')] = 'accept'

#update the transition table for the following token: book
transition_table[('q22','b')] = 'q23'
transition_table[('q23','o')] = 'q24'
transition_table[('q24','o')] = 'q25'
transition_table[('q25','k')] = 'q26'
transition_table[('q26',' ')] = 'q41'
transition_table[('q26','#')] = 'accept'
transition_table[('q41',' ')] = 'q41'
transition_table[('q41','#')] = 'accept'

#update the transition table for the following token: blouse
transition_table[('q22','b')] = 'q23'
transition_table[('q23','l')] = 'q27'
transition_table[('q27','o')] = 'q28'
transition_table[('q28','u')] = 'q29'
transition_table[('q29','s')] = 'q30'
transition_table[('q30','e')] = 'q31'
transition_table[('q31',' ')] = 'q41'
transition_table[('q31','#')] = 'accept'
transition_table[('q41',' ')] = 'q41'
transition_table[('q41','#')] = 'accept'

#update the transition table for the following token: banana
transition_table[('q22','b')] = 'q23'
transition_table[('q23','a')] = 'q32'
transition_table[('q32','n')] = 'q33'
transition_table[('q33','a')] = 'q34'
transition_table[('q34','n')] = 'q35'
transition_table[('q35','a')] = 'q36'
transition_table[('q36',' ')] = 'q41'
transition_table[('q36','#')] = 'accept'
transition_table[('q41',' ')] = 'q41'
transition_table[('q41','#')] = 'accept'

#update the transition table for the following token: berry
transition_table[('q22','b')] = 'q23'
transition_table[('q23','e')] = 'q37'
transition_table[('q37','r')] = 'q38'
transition_table[('q38','r')] = 'q39'
transition_table[('q39','y')] = 'q40'
transition_table[('q40',' ')] = 'q41'
transition_table[('q40','#')] = 'accept'
transition_table[('q41',' ')] = 'q41'
transition_table[('q41','#')] = 'accept'

#transition for new token
transition_table[('q0','p')] ='q12'
transition_table[('q0','b')] ='q23'

transition_table[('q11','m')] ='q1'
transition_table[('q11','b')] ='q23'

transition_table[('q22','m')] ='q1'
transition_table[('q22','p')] ='q12'

transition_table[('q41','b')] ='q23'
transition_table[('q41','m')] ='q1'
transition_table[('q41','p')] ='q12'

#lexical analysis
idx_char = 0
state = 'q0'
current_token =' '
while state!='accept':
    current_char = input_string [idx_char]
    current_token += current_char
    state = transition_table[(state, current_char)]
    if state=='q11':
        print (' current token: ', current_token, ', valid')
        current_token = ' '
    if state=='q22':
        print (' current token: ', current_token, ', valid')
        current_token = ' '
    if state=='q41':
        print (' current token: ', current_token, ', valid')
        current_token = ' '
    if state == 'error':
        print ('eror')
        break;
    idx_char = idx_char + 1

# conclusion
if state=='accept' :
    print (' semua token di input: ', sentence, ', valid' )