# 유전체 분석 실습

https://github.com/KennethJHan/GenomeAnalysisTutorial     #생물정보학 Github Repository

#유전체 분석 유튜브 강의

https://www.youtube.com/watch?v=6GJ3GqkUK94&list=PL_4hJwdNSJ28pEXoHafBAW8m0mSkumPrC

유튜브 강의를 통해 11개의 목차를 마쳤다.

유전체 분석 도서를 찾아보다가 "바이오 파이썬으로 만나는 생물정보학"를 알게되어 구매했다.

![image](https://user-images.githubusercontent.com/69448218/209437035-0264a8ce-9f06-413b-9f89-de35d1d518a1.png)

시작해보자

준비하기
-
필요한 데이터는 git clone 명령어로 아래의 git Repository에서 다운로드 받는다

git clone https://github.com/KennethJHan/GenomeAnalysisTutorial.git

상기의 명령어를 입력했을 때 -bash: git: command not found 문구가 뜨면 git이 설치되지 않은 것이다
OS가 CentOS이면 아래의 명령어로 설치를 진행한다.

<pre><code>
yum install git
</code></pre>
  
/GenomeAnalysisTutorial/resource/reference 경로에 들어가서 gz압축파일을 푼다

gunzip hg38.chr21.fa.bwt.2bit.64.gz

Tool 설치
-

1. BWA2

mkdir명령어로 tool 디렉터리를 생성하고, BWA tool을 설치한다

<pre><code>
mkdir tool
curl -L https://github.com/bwa-mem2/bwa-mem2/releases/download/v2.0pre2/bwa-mem2-2.0pre2_x64-linux.tar.bz2  | tar jxf -
</code></pre>

설치 후 ./bwa-mem2 명령어로 확인한다.

![bwa-mem2 설치 후 명령어](https://github.com/Hoon-it/Bioinformatics/assets/69448218/d1b787a8-2868-410b-89e4-f77d09b20b9e)

2. samtools 설치

구글에 samtools를 검색하고 보이는 첫번째 링크를 클릭하고 우측 상단에 다운로드 클릭하면 보이는 Downloads를 클릭한다

클릭 후 보이는 Download current source releases: 에서 samtools-1.18 초록색 버튼을 우클릭후 링크 주소 복사를 클릭한다.

그리고 복사된 주소 링크를 리눅스 터미널 창에 붙여넣기한다.  #붙여넣기 하기 전에 which 명령어로 samtools가 설치되어 있는지 확인한다.

<pre><code>
which samtools
</code></pre>

아무런 반응이 없으면 설치되어 있지 않은 것이다.

<pre><code>
wget https://github.com/samtools/samtools/releases/download/1.18/samtools-1.18.tar.bz2
</code></pre>

#해당 명령어로 samtools를 다운로드 받고 ll명령어로 확인한다.

tar 파일이기에 tar xvf로 압축해제한다.

<pre><code>
tar xvf samtools-1.18.tar.bz2
</code></pre>

압축해제 후 ll명령어로 다시 확인한다.

압축해제 후 samtools 폴더에 들어가서 ./configure 명령어로 잘 설치되었는지 확인한다.

![samtools configure 명령어](https://github.com/Hoon-it/Bioinformatics/assets/69448218/14b5bee8-e1e9-4275-bdf3-4068e71c6da9)

추가로 make -> make install 명령어 순서로 설치를 진행한다.

![make 명령어](https://github.com/Hoon-it/Bioinformatics/assets/69448218/352293af-6def-48e0-be7a-04c961edf682)

설치 마무리 후 which samtools 명령어를 입력하면 설치된 위치를 알 수 있고, samtools 명령어를 실행하면 아래의 이미지와 같이 Program, Version, Usage...가 나오면 마무리 된것이다.

![samtools 설치 마무리 후 확인 명령어](https://github.com/Hoon-it/Bioinformatics/assets/69448218/d2ba0ad7-3a56-4ef8-ad0d-6e9bbc48725e)

BAM 파일 보는 명령어
-
아래의 명령어로 bam파일과 bam.index 파일을 다운받는다.

<pre><code>
wget https://github.com/KennethJHan/Genome-Analysis-Tutorial/raw/master/result/SRR000982.mapped.sorted.markdup.bam
</code></pre>

<pre><code>
wget https://github.com/KennethJHan/Genome-Analysis-Tutorial/raw/master/result/SRR000982.mapped.sorted.markdup.bam.bai
</code></pre>
  
![bam파일 보는 명령어v2](https://github.com/Hoon-it/Bioinformatics/assets/69448218/e3120440-31c1-4a20-ab77-c21c4e67e17d)

samtools를 설치한 뒤 samtools tview SRR000982.mapped.sorted.bam 명령어를 실행하면

![bam 파일](https://github.com/Hoon-it/Bioinformatics/assets/69448218/2a81c931-2812-4b27-9811-5b7cce15b8c6)

상기의 이미지에서 리드가 쌓여 있는 보이고 shift + ? 를 누르면 추가적인 명령어를 볼 수 있다. 그리고 /를 누르면

![원하는 크로모좀 위치](https://github.com/Hoon-it/Bioinformatics/assets/69448218/b6502d1b-04a6-4c72-9f2c-ac117e13ed89)

원하는 크로모좀 몇번의 어느위치로 이동할 수 있다. [Goto: chr1:111]

fastq.gz의 전체 라인 개수 확인 방법

[root@LdapClient data]# zcat [sample_1.fastq.gz] | wc -l

328476

전체 라인 개수에서 나누기 4를 하면 리드 개수를 알 수 있다.

fastq.gz 파일 보는 방법
-
zless -S sample_1.fastq.gz

![zless -S 명령어](https://github.com/Hoon-it/Bioinformatics/assets/69448218/16cb8190-c66e-47bc-ba11-aea341269220)

상기의 명령어를 입력하면 아래와 같이 파일이 열린다

![zless명령어v2](https://github.com/Hoon-it/Bioinformatics/assets/69448218/5a3d6a4c-52fc-4056-b158-c6fa2aa6aa00)

네개의 줄이 하나의 리드로 작성되어 있다
1번째는 헤더, 2번째 줄은 서열, 3번째는 구분자 역할, 4번째는 서열에 대한 퀄리티 점수

레퍼런스(hg38.chr21.fa)에 대한 인덱스 파일 생성하는 법
-
![BWA2 명령어 실패](https://github.com/Hoon-it/Bioinformatics/assets/69448218/bdc1b4ce-7a56-4261-ae11-f0275e8c6126)

hg38.chr21.fa.bwt.8bit.32 파일이 없어서 발생한 에러

hg38.chr21.fa이 있는 경로에 가서

$BWA2 index hg38.chr21.fa 명령어를 실행한다.  #시간이 조금 걸리고 RAM이 2GB 안되는 용량이 필요하다...

상기의 명령어를 입력하면 [hg38.chr21.fa.bwt.8bit.32]와 같은 파일이 생성된다.

![인덱스 파일 생성 후](https://github.com/Hoon-it/Bioinformatics/assets/69448218/f35b8c32-f24a-4ca3-92ce-13d80b0f12cf)

생성되었으면 레퍼런스 서열에 리드를 매핑하는 작업을 한다.

$BWA2 mem -t 1 -R "@RG\tID:sample\tSM:sample\tPL:platform" ../resource/reference/hg38.chr21.fa sample_1.fastq.gz sample_2.fastq.gz > sample.mapped.sam

![$BWA@ mem -t 명령어 입력 후](https://github.com/Hoon-it/Bioinformatics/assets/69448218/9657f40c-9e80-4c95-b7a3-83fc2b312849)

sam파일을 bam파일로 바꾸는 명령어

$SAMTOOLS view -Sb sample.mapped.sam > sample.mapped.bam

bam파일 보는 명령어

$SAMTOOLS view -h sample.mapped.bam | less -S

![매핑 후 bam 파일edit](https://github.com/Hoon-it/Bioinformatics/assets/69448218/e3a7ebfc-3f55-4c69-bc03-aa3382cb0c06)

#sam은 텍스트파일이고, bam은 압축해서 바이너리 형태로 만든 파일이다 압축을 하는 이유 실습파일은 파일 용량이 적지만 실제 업무에서나 연구에서 사용하는 파일은
기하급수적으로 용량이 커져서 단순히 sam으로는 사용할 수 없어서 bam으로 바꾼다.

Samtools Command
-
![samtools 명령어](https://github.com/Hoon-it/Bioinformatics/assets/69448218/35d2160d-bc77-4cd5-8c79-bca8968be40e)

Duplication Marking 순서
-
fixmate -> sort -> markdup

$SAMTOOLS fixmate -m sample.mapped.bam sample.fixmate.bam

$SAMTOOLS sort -o sample.fixmate.sorted.bam sample.fixmate.bam

$SAMTOOLS markdup sample.fixmate.sorted.bam sample.markdup.bam

![fix-sort-markup](https://github.com/Hoon-it/Bioinformatics/assets/69448218/8bb60c57-4df2-4ad2-94a3-3403e4247494)
총 3단계를 거치면 duplication을 마킹한 bam이 나온다.

실제로 bam에 duplication 마킹되었는지 확인하는 방법

$SAMTOOLS view -h sample.markdup.bam | less -S

@HD, @SQ, @RG : 헤더      SRR1518~.1609941 : 리드  .1609941 : 리드      리드이름 우측 숫자(SAM flag) : 129,65,81...

![markdup bam 파일](https://github.com/Hoon-it/Bioinformatics/assets/69448218/4302a064-63d2-4e5e-9b22-4acef8f0381e)

SAM flag 홈페이지에 접속해서 숫자를 입력하면 리드에 대한 정보를 알 수 있다.

$SAMTOOLS view -h -f 1024 sample.markdup.bam | less -S      #-f [1024] 옵션 : 해당 플래그 번호를 포함한 정보를 보고 싶을때 사용하는 옵션

$SAMTOOLS view -h -F 1024 sample.markdup.bam | less -S      #-F [1024] 옵션 : 해당 플래그 번호를 포함하지 않은 정보를 보고 싶을때 사용하는 옵션

$SAMTOOLS view -h sample.markdup.bam | less -S      #-h 옵션 : 헤더와 리드가 같이 나온다

$SAMTOOLS view -H sample.markdup.bam | less -S      #-H : 헤더만 나온다

$SAMTOOLS view sample.markdup.bam | less -S      # 옵션이 없으면 리드만 나온다

$SAMTOOLS view sample.markdup.bam | wc -l      #전체 라인 개수(전체 리드 개수)가 나온다

$SAMTOOLS view -f 1024 sample.markdup.bam | wc -l      #duplicate가 있는 라인이 출력

markdup.bam index 파일 생성
-
$SAMTOOLS index sample.markdup.bam

tview 옵션 : 리드가 쌓인것을 볼 수 있게 해주는 옵션
