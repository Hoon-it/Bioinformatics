# 유전체 분석 실습

https://github.com/KennethJHan/GenomeAnalysisTutorial     #생물정보학 Github Repository

https://www.youtube.com/watch?v=6GJ3GqkUK94&list=PL_4hJwdNSJ28pEXoHafBAW8m0mSkumPrC #유전체 분석 유튜브 강의

유튜브 강의를 통해 11개의 목차를 마쳤다.

유전체 분석 도서를 찾아보다가 "바이오 파이썬으로 만나는 생물정보학"를 알게되어 구매했다.

![image](https://user-images.githubusercontent.com/69448218/209437035-0264a8ce-9f06-413b-9f89-de35d1d518a1.png)

시작해보자

BAM 파일 보는 명령어
-
![bam파일 보는 명령어v2](https://github.com/Hoon-it/Bioinformatics/assets/69448218/e3120440-31c1-4a20-ab77-c21c4e67e17d)

samtools를 설치한 뒤 samtools tview SRR000982.mapped.sorted.bam 명령어를 실행하면

![bam 파일](https://github.com/Hoon-it/Bioinformatics/assets/69448218/2a81c931-2812-4b27-9811-5b7cce15b8c6)

상기의 화면이 보이고 shift + ? 를 누르면 추가적인 명령어를 볼 수 있다. 그리고 /를 누르면

![원하는 크로모좀 위치](https://github.com/Hoon-it/Bioinformatics/assets/69448218/b6502d1b-04a6-4c72-9f2c-ac117e13ed89)

원하는 크로모좀 몇번의 어느위치로 이동할 수 있다.

fastq.gz의 전체 라인 개수 확인 방법

[root@LdapClient data]# zcat [sample_1.fastq.gz] | wc -l

328476

전체 라인 개수에서 나누기 4를 하면 리드 개수를 알 수 있다.

fastq.gz 파일 보는 방법

zless -S sample_1.fastq.gz

상기의 명령어를 입력하면 아래와 같이 파일이 열린다

![zless명령어v2](https://github.com/Hoon-it/Bioinformatics/assets/69448218/5a3d6a4c-52fc-4056-b158-c6fa2aa6aa00)

네개의 줄이 하나의 리드로 작성되어 있다
1번째는 헤더, 2번째 줄은 서열, 3번째는 구분자 역할, 4번째는 서열에 대한 퀄리티 점수

레퍼런스(hg38.chr21.fa)에 대한 인덱스 파일 생성하는 법
-
$BWA2 index hg38.chr21.fa  #시간이 조금 걸리고 RAM이 2GB 안되는 용량이 필요하다...

상기의 명령어를 입력하면 [hg38.chr21.fa.bwt.8bit.32]와 같은 파일이 생성된다.
