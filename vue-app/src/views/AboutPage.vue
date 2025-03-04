<template>
  <div>
    <h3 style="font-size: 2rem;">오케스트레이터 소개</h3>
    
    <section>
      <div class="small-break"></div>
      <h4 style="font-size: 1.5rem;">프로젝트 개요</h4>
      <p style="font-size: 0.9rem;">
        본 프로젝트는 Orchestrator &amp; Workflow Manager를 별도의 서비스로 구축하여, 
        유저와 대화 데이터 관리, 대화 내용 분석을 통한 AI agent 배분, 
        그리고 시스템 운영 모니터링을 실현하는 것을 목표로 합니다.
      </p>
    </section>

    <section>
      <div class="small-break"></div>
      <h4 style="font-size: 1.5rem;">주요 기능 상세</h4>
      
      <h5 style="font-size: 1.3rem;">1. 데이터 관리 및 유저 기능</h5>
      <ul style="font-size: 0.9rem; margin-left: 1.5rem;">
        <li>Django Admin을 통한 유저 로그인 및 DB 관리</li>
        <li>Nginx와 Daphne를 통한 요청 처리 및 input 적재</li>
        <li>유저 메타 정보 조회 (아이디, 질문 목록, 자격 증명, 세션 정보, 유저 로그 등) 및 필터링</li>
      </ul>

      <h5 style="font-size: 1.3rem;">2. 대화 분석 및 AI 배분</h5>
      <ul style="font-size: 0.9rem; margin-left: 1.5rem;">
        <li>Workflow Manager를 통해 DB의 대화 내용 분석</li>
        <li>인메모리 context 관리 및 CRUD 기능으로 로직 흐름 유지</li>
        <li>분석 결과에 따라 적절한 AI agent에 배분 및 실행 (Orchestrator)</li>
      </ul>

      <h5 style="font-size: 1.3rem;">3. 운영 관리</h5>
      <ul style="font-size: 0.9rem; margin-left: 1.5rem;">
        <li>Django 기반 admin 유저 로그인 기능</li>
        <li>Prometheus와 Grafana를 통한 시스템 리소스 모니터링</li>
      </ul>

      <h5 style="font-size: 1.3rem;">4. 보안 및 향후 확장</h5>
      <ul style="font-size: 0.9rem; margin-left: 1.5rem;">
        <li>보안 관련 세부 사항은 추후 추가 예정 (TBD)</li>
        <li>Chat 기반 sub-test 기능 구현 고려 (대화 화면, 입력/출력 통제 및 스트리밍 기능 포함)</li>
      </ul>
    </section>

    <section>
      <div class="small-break"></div>
      <h4 style="font-size: 1.5rem;">서버 구축 및 기술 스택</h4>
      <ul style="font-size: 0.9rem; margin-left: 1.5rem;">
        <li><strong>Frontend:</strong> Vue.js</li>
        <li><strong>Backend:</strong> Django, Daphne</li>
        <li><strong>Database:</strong> PostgreSQL</li>
        <li><strong>인프라/캐싱:</strong> Redis, Nginx, Docker</li>
        <li><strong>모니터링:</strong> Prometheus, Grafana</li>
      </ul>
    </section>
  </div>
</template>

<script>
export default {
  name: "AboutPage",
};
</script>

<style scoped>
/* Add component-specific styles if needed */
</style>
