# 프로젝트: 비랩트(BeRapt) 공식 홈페이지 리뉴얼 가이드

## 1. 기업 아이덴티티 (Company Identity)
- **회사명:** 주식회사 비랩트 (BeRapt)
- **비전:** "창작자가 그림만 그려도 자립할 수 있는 서브컬처 생태계 조성"
- **슬로건:** Empowering Creators, Enriching Fandom.
- **핵심 가치:** 1. **수익화:** 이미지 창작자를 위한 조회수 및 구독 기반 수익 모델 제공.
    2. **소장 가치:** 디지털 콘텐츠의 실물 자산화(OCC)를 통한 팬덤 경험 확장.
    3. **상생:** AI를 도구로 활용하여 창작자의 권익과 생산성을 동시에 보호.

## 2. 주요 서비스 모델 (Core Business Model)

### ① ShoulderPick (숄더픽)
- **정체성:** "일러스트레이터판 유튜브" (오픈 플랫폼)
- **수익 구조:** - 창작자가 그림을 등록하면 팬들의 조회수와 관심도(Pick) 데이터에 따라 수익 배분.
    - 별도의 영업 없이 콘텐츠 파워만으로 수익을 창출하는 간접 수익 모델.

### ② Shoulder (숄더)
- **정체성:** "유튜브 멤버십형 폐쇄 커뮤니티" (구독 플랫폼)
- **수익 구조:** - 유료 구독자 전용 한정 콘텐츠(미공개 시안, 고화질 원본 등) 제공.
    - 작가와 팬 사이의 밀착 소통을 지원하며 안정적인 월간 정기 수익(Direct Revenue) 발생.

## 3. Solution: OCC (Original Collection Card) 상품 라인업
실물 굿즈 판매를 통해 디지털 IP의 가치를 극대화합니다.

| 구분 | 상품명 | 특징 및 컨셉 | 상태 | 판매 링크 |
| :--- | :--- | :--- | :--- | :--- |
| **Season 1** | 오리지널 컬렉션 Vol.1 | 비랩트 생태계의 시작을 알린 초기 한정판 컬렉션 | 판매 중 | [Link] |
| **Season 2** | 오리지널 컬렉션 Vol.2 | 참여 작가군 확대 및 프리미엄 특수 가공 적용 | 주력 판매 | [Link] |
| **Season 3** | 오리지널 컬렉션 Vol.3 | 최신 인기 IP 및 신규 일러스트 라인업 | **NEW** | [Link] |

## 4. 홈페이지 섹션 구성 및 디자인 가이드

### [Section 1] Hero Section
- **컨셉:** 'Pick' 버튼과 'Membership' 배지가 강조된 일러스트레이터의 작업 공간 시각화.
- **카피:** "당신의 그림이 데이터가 되고, 데이터가 수익이 되는 곳."

### [Section 2] Platform Dual-Core
- **좌측 (ShoulderPick):** 조회수 기반 수익 그래프 및 투표 UI 컴포넌트 배치.
- **우측 (Shoulder):** 'Unlock' 효과가 들어간 멤버십 전용 콘텐츠 카드 배치.

### [Section 3] OCC Showcase (Solution)
- **디자인:** 시즌 1, 2, 3 카드를 나란히 배치한 그리드 레이아웃.
- **인터랙션:** 카드 마우스 오버 시 입체적인 회전 효과(3D Flip) 및 홀로그램 효과 적용.
- **버튼:** 각 카드 하단에 강렬한 CTA(Call to Action) '소장하기' 또는 'Buy Now' 버튼 배치.

### [Section 4] Activities
- **디자인:** images/off_events 폴더안의 이미지들을 랜덤 카드배열
- **인터렉션** 마우스 오버하면 살짝 확대. 클릭하면 크게볼 수 있게.

### [Section 5] Partners & History
- 일본 최대 플랫폼 '아무타스' 투자 유치 및 주요 유통 파트너사 로고 배치.

### [Section 6] News
- 비랩트, ‘창구 프로그램 7기’ 선정 : https://it.chosun.com/news/articleView.html?idxno=2023092139155
- 비랩트, 일본 아무타스로부터 PreA 투자유치 : https://biz.chosun.com/it-science/ict/2024/01/25/MHERS6BPHBG4RKEPKBDTWU5YTI/
- 작가 응원 커뮤니티 ‘숄더’ 운영사 비랩트, 중기부 팁스(TIPS)에 선정 : https://www.nextdaily.co.kr/news/articleView.html?idxno=219942

## 5. 기술 스택 (Technical Stack)
- **Frontend:** React, Next.js (SEO 최적화)
- **Styling:** Tailwind CSS (서브컬처 감성의 다크/화이트 모드)
- **Animation:** Framer Motion (카드 효과 및 섹션 전환)
- **Design:** Figma (MCP 연동을 통한 컴포넌트 관리)
