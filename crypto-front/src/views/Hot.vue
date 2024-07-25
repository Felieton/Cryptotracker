<template>
  <div id="currencies-hot" style="margin-bottom:5%">
    <CryptoTable :items=items />
  </div>
</template>

<script>

import CryptoTable from '/src/components/CryptoTable.vue'
import axios from 'axios'

export default {
  name: "Hot",
  components: {
    CryptoTable,
  },
  data() {
    return {
      items: [],
      resultsData: []
    }
  },
  methods: {
    async getCurrencies() {
      const url = "http://localhost:5000/CryptoCurrency/get_hot_currencies";
      const data = {
        meta: {
          method: "get_hot_currencies",
          args: {
          },
        },
        };
      axios.post(url, data).then(
        (response) => {
            console.log(response);
          for (let index = 0; index < response.data.meta.result.result.length; ++index) {
            this.resultsData.push(
              response.data.meta.result.result[index].attributes
            ); // ???
            let variant = "info";
            if (this.resultsData[index]["price_change"] < 0) {
              variant = "danger"
            }
            let item = {
              code: this.resultsData[index]["code"],
              image: this.resultsData[index]["logo_url"],
              name: this.resultsData[index]["name"] + " " + this.resultsData[index]["code"],
              price: "$" + this.resultsData[index]["price"],
              price_change: this.resultsData[index]["price_change"] + " (" + Math.round(this.resultsData[index]["price_change_pct"] 
              * 10000) / 100 + "%)",
              market_cap: Math.round(this.resultsData[index]["market_cap"] / 1000000) + "M",
              volume: Math.round(this.resultsData[index]["volume"] / 1000000) + "M",
              _rowVariant: variant
            };
            this.items.push(item);
            console.log(item);
          }
        },
        (error) => {
          console.log(error);
        }
      );
    },
  },

  mounted() {
    this.getCurrencies();
  }
};
</script>

<style scoped>
.red-oblique-text {
  color: red;
  font-style: oblique;
}
.add-book-button {
  float: right;
} 
</style>