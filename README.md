# 대전 눈썹문신 홈페이지 시안

정적 HTML 6페이지(홈 + 세부 5개)입니다. CSS, JS, 이미지는 `assets/`에 분리했습니다. 상호 `결담 브로우`는 임시로 설정한 가상 상호이며 실제 업체의 시술 사례나 운영 정보를 주장하지 않습니다.

피부샵의 차분한 공간감을 기준으로 홈과 세부페이지 전체를 다시 디자인했습니다. 얼굴 클로즈업 대신 상담 공간·브로우 도구·색상·관리 장면의 서로 다른 정사각 사진 5장을 사용합니다.

메인 최상단에는 새로 제공된 `홈페이지 임대문의.png` 이미지를 원본 그대로 배치했으며, 이미지 전체를 누르면 `https://pf.kakao.com/_QqyKn`으로 이동합니다. 모바일에서는 이미지를 자르지 않고 전체 표시하며, 작은 화면에서 읽기 쉽도록 이미지 아래에 큰 글씨와 문의 버튼을 추가했습니다. `rss.xml`은 홈과 세부페이지 5개의 현재 목록을 담고 있습니다. 새 글을 발행하면 피드 항목을 추가해야 합니다.

`llms.txt`는 사이트의 주요 페이지를 간단히 설명하고 연결합니다. 배포 주소가 정해지면 `SITE_URL`을 설정해 다시 생성하세요. 파일을 추가했다고 AI 검색 노출이 보장되지는 않습니다.

## 배포 전에 반드시 설정할 항목

1. 실제 상호, 상담 채널, 운영 정보, 시술 범위를 확정하고 표시 문구를 교체하세요. 지금 시안에는 가상의 주소, 후기, 가격, 자격, 전화번호를 넣지 않았습니다.
2. 배포 주소를 정한 뒤 프로젝트 루트에서 `SITE_URL=https://실제-도메인 python3 build.py`를 실행하세요. 이 명령이 모든 페이지의 canonical, Open Graph, 홈의 ItemList, sitemap, robots URL을 동일한 실제 주소로 생성합니다. 배포 시 `SITE_URL`을 실제 도메인과 일치시켜 주세요.
3. ZIP을 풀었을 때 **최상단에 `index.html`, `rss.xml`, `llms.txt`, `assets/`가 바로 보여야 합니다.** 이 파일들을 GitHub 저장소 루트에 올리고 Cloudflare Pages에서 해당 저장소를 연결합니다. Framework preset은 None, Build command는 `SITE_URL=https://실제-도메인 python3 build.py`, Build output directory는 `.`입니다. `SITE_URL`을 Pages 환경 변수로 지정했다면 Build command는 `python3 build.py`로 설정해도 됩니다. 커스텀 도메인을 연결하거나 Pages 주소가 바뀌면 다시 빌드하세요.
4. 실제 시술 서비스의 의료·광고 관련 문구와 사업자 정보는 운영자가 확인한 사실로 교체하세요.

배포 후 `https://실제-도메인/rss.xml`과 `https://실제-도메인/llms.txt`를 직접 열어 확인하세요. GitHub 저장소에 `daejeon-brow-site/` 폴더째 올렸다면 Build output directory를 `daejeon-brow-site`로 바꾸거나, 폴더 안의 파일을 저장소 루트로 이동해야 합니다. `SITE_URL`의 값이 잘못돼도 XML 파일의 링크가 잘못될 뿐, `/rss.xml` 자체의 404 원인은 아닙니다.

## 캐러셀 구현

홈 `<head>` 상단에 `ItemList` JSON-LD가 있으며, 다섯 개의 카드가 각각 실제 세부페이지 URL과 서로 다른 원본 생성 이미지 URL을 가리킵니다. 화면에는 같은 항목의 가로 스크롤 카드가 표시됩니다. 네이버 검색 결과의 캐러셀 노출은 검색엔진 판단에 따르며 보장되지 않습니다. 첨부한 성공 사례의 Owl Carousel 스크립트는 화면 애니메이션용이며 해당 소스 자체에는 `ItemList` JSON-LD가 확인되지 않았습니다.

## 파일 구조

- `index.html`: 홈
- `natural/`, `soft-arch/`, `color/`, `process/`, `aftercare/`: 세부페이지
- `assets/css/style.css`, `assets/js/site.js`: 스타일과 동작
- `assets/images/`: 직접 생성한 이미지 5개
- `assets/images/lease-inquiry.png`: 제공된 메인 이미지 원본
- `rss.xml`: 현재 6개 페이지의 RSS 2.0 피드
- `llms.txt`: 주요 페이지의 간결한 안내와 링크
- `build.py`: 배포 주소를 반영한 정적 페이지 생성
