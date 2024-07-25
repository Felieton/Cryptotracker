<template>
  <div>
    <div class="crypto-chart">
        <canvas ref="cryptoChart"></canvas>
    </div>
  </div>
</template>

<script>
import Chart from "chart.js";
export default {
  name: "CryptoChart",
  props: {
    currency_history: [],
  },
  methods: {
    getChartData() { 
      for (let index = 0; index < this.currency_history.length; ++index) {
            this.prices.push(this.currency_history[index].attributes.price);
            this.dates.push(this.currency_history[index].attributes.price_timestamp);
      }
    },
    renderCryptoChart() {
        var chartData = {
                    labels: [],
                    datasets: [
                        {
                            label: this.currency_history[0].attributes.name,
                            data: [],
                            backgroundColor: "#42b983"
                        },
                    ],
                };
        for (let entry of this.currency_history) {
            chartData.labels.push(entry.attributes.price_timestamp);
            chartData.datasets[0].data.push(entry.attributes.price);
        }
        var ctx = this.$refs.cryptoChart.getContext("2d");
        this.chart = new Chart(ctx, {
            type: "line",
            data: chartData,
            options: {
                scales: {
                    xAxes: [
                        {
                            offset: true,
                            scaleLabel: {
                                display: true,
                                labelString: "Date [YYYY-MM-DD]",
                            },
                        },
                    ],
                    yAxes: [
                        {
                            scaleLabel: {
                                display: true,
                                labelString: "Price",
                            },
                        },
                    ],
                },
            },
        });
    }
  },
  data() {
    return {
      prices: [],
      dates: [],

    };
  },
  mounted() {
    this.renderCryptoChart();
  }
};
</script>

<style scoped>
 .crypto-chart {
        width:500px;
    }
</style>