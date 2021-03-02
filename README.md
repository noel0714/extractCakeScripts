# extractCakeScripts
## Installation
  + request
  + BeautifulSoup

## Explanation
  + 영어회화 앱 Cake에서 영어, 한글 스크립트를 크롤링 해 옴
  + 크롤링한 스크립트를 Tistory 블로그의 테이블 형식으로 바꿔 줌

## Usage
  + main 함수 안 URL 변수에 Cake 앱 동영상 플레이 웹페이지 주소를 넣어주고 실행하면 result.txt.에 스크립트가 저장됨
  + Tistory 블로그에서 글쓰기 항목을 클릭
  + 테이블 생성 후 F12 클릭
  + HTML source 중 <tbody> 항목을 찾아서 result.txt 안에 저장된 스크립트로 교체해 주면 됨

## Etc
  + 요청해 주시면 다른 블로그 형식도 만들어 드릴게요!
