from django.shortcuts import render


def crawler(request):
    return render(request, 'crawler/crawler.html')

# 크롤링을 하겠다는 리퀘스트와 json 형식의 텍스트를 넘겨받음
# 해당하는 이미지를 모델 및 폴더에 저장
# 페이지를 새로고침 시키고 받은 이미지들이 표시됨
