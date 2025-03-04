<template>
  <div>
    <h3 style="font-size: 2rem;">오케스트레이터</h3>
    <p style="font-size: 1rem;">
      Orchestrator &amp; Workflow Manager를 통한 대화 데이터 관리 및 AI agent 배분 서비스입니다.
    </p>

    <section>
      <div class="small-break"></div>
      <h4 style="font-size: 1.5rem;">서비스 목표</h4>
      <p style="font-size: 0.9rem;">
        유저와 대화 내용의 효율적인 관리, 대화 분석을 통한 AI agent 배분, 그리고 운영 서비스 관리를 목표로 합니다.
      </p>
    </section>

    <section>
      <div class="small-break"></div>
      <h4 style="font-size: 1.5rem;">핵심 기능</h4>
      <ul style="font-size: 0.9rem; margin-left: 1.5rem;">
        <li>유저 ↔ 대화 내용 DB 관리 (Django Admin, Nginx, Daphne 등)</li>
        <li>대화 분석 및 AI agent 배분 (Workflow Manager &amp; Orchestrator)</li>
        <li>시스템 리소스 모니터링 (Prometheus, Grafana)</li>
        <li>향후 Chat 기반 sub-test 기능 (대화 스트리밍 등)</li>
      </ul>
    </section>

    <div class="small-break"></div>
    <p style="font-size: 0.9rem;">
      더 자세한 정보를 원하시면 
      <router-link to="/about" style="font-size: 0.9rem;">About</router-link>
      페이지를 확인해 주세요.
    </p>
  </div>
</template>

<script>
export default {
  name: "HomePage",
};
</script>

<style scoped>
/* Add component-specific styles if needed */
</style>
