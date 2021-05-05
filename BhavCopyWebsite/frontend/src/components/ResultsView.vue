<template>
  <div style="position: relative">
    <button type="button" class="btn btn-primary mb-2" @click="downloadCSVData">
      Download CSV of Results
    </button>

    <div class="table-wrapper">
      <table class="table">
        <thead>
          <tr>
            <th>Code</th>
            <th>Name</th>
            <th>Open</th>
            <th>High</th>
            <th>Low</th>
            <th>Close</th>
          </tr>
        </thead>
        <tbody v-for="scrip in scrips" :key="scrip.name">
          <tr>
            <td>{{ scrip.code }}</td>
            <td>{{ scrip.name }}</td>
            <td>{{ scrip.open }}</td>
            <td>{{ scrip.high }}</td>
            <td>{{ scrip.low }}</td>
            <td>{{ scrip.close }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: "ResultsView",
  props: {
    scrips: {
      type: Array,
      default: () => [],
    },
  },
  methods: {
    downloadCSVData() {
      let csv = "Code,Name,Open,High,Low,Close\n";
      this.scrips.forEach((scrip) => {
        csv += `${scrip.code},${scrip.name},${scrip.open},${scrip.high},${scrip.low},${scrip.close}\n`;
      });
      const anchor = document.createElement("a");
      anchor.href = "data:text/csv;charset=utf-8," + encodeURIComponent(csv);
      anchor.target = "_blank";
      anchor.download = `Stocks.csv`;
      anchor.click();
    },
  },
};
</script>

<style scoped>
table {
  width: 100%;
}
.table-wrapper {
  overflow: auto;
}
</style>
