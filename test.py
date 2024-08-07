from sentence_sim import SentenceSim
from rouge import ko_rouge
from bleu import calc_bleu
from colorama import Fore, Style, init

sentencesim = SentenceSim()

label_sentence = '나는 아침으로 김치찌개를 먹었습니다.'
compare_sentence_1 = '우리 아빠는 매일 아침으로 김치찌개를 드십니다.'
compare_sentence_2 = '오늘 회사 구내식당의 메뉴로 나온 김치찌개는 매우 맛이 없었습니다.'

print(Fore.GREEN + Style.BRIGHT + 'KoDiffCSE 문장 유사도 계산' + Style.RESET_ALL)
print(f'문장1:{label_sentence}\n문장2:{compare_sentence_1}\n유사도:{sentencesim.cal_score(label_sentence,compare_sentence_1)}', end='\n\n')
print(f'문장1:{label_sentence}\n문장2:{compare_sentence_2}\n유사도:{sentencesim.cal_score(label_sentence,compare_sentence_2)}', end='\n\n')

print(Fore.GREEN + Style.BRIGHT + 'rouge 문장 유사도 계산' + Style.RESET_ALL)
print(f'문장1:{label_sentence}\n문장2:{compare_sentence_1}\n유사도:{ko_rouge(label_sentence,compare_sentence_1)}', end='\n\n')
print(f'문장1:{label_sentence}\n문장2:{compare_sentence_2}\n유사도:{ko_rouge(label_sentence,compare_sentence_2)}', end='\n\n')

print(Fore.GREEN + Style.BRIGHT + 'bleu 문장 유사도 계산' + Style.RESET_ALL)
print(f'문장1:{label_sentence}\n문장2:{compare_sentence_1}\n유사도:{calc_bleu(label_sentence,compare_sentence_1)}', end='\n\n')
print(f'문장1:{label_sentence}\n문장2:{compare_sentence_2}\n유사도:{calc_bleu(label_sentence,compare_sentence_2)}', end='\n\n')