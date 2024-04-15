# nlp_tools
simple tools for natural language processing

### 문장 유사도 계산기

```python
from sentence_sim import SentenceSim

sentencesim = SentenceSim()

label_sentence = '나는 아침으로 김치찌개를 먹었습니다.'
compare_sentence_1 = '우리 아빠는 매일 아침으로 김치찌개를 드십니다.'
compare_sentence_2 = '오늘 회사 구내식당의 메뉴로 나온 김치찌개는 매우 맛이 없었습니다.'

print(f'유사도(1번):{sentencesim.cal_score(label_sentence,compare_sentence_1)}', end='\n\n')

print(f'유사도(2번):{sentencesim.cal_score(label_sentence,compare_sentence_2)}', end='\n\n')
```
