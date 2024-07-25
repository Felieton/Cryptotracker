<template>
  <div>
    <div style="display:inline-block;vertical-align:top;margin-left:20%;margin-top:0%;">
      <img style="width:100px" v-bind:src="currency.logo_url">
    </div>
    <div style="display:inline-block;margin-top:1%">
      <div class="name">{{currency.name}}</div>
    </div>
    <div style="display:inline-block;margin-top:0.5%;margin-left:1%">
      <div>{{currency.code}}</div>
    </div>
    <div style="display:inline-block;margin-top:0.5%;margin-left:1.5%">
      <div class="price">{{Math.round(currency.price * 100)/100}}$</div>
    </div>
    <div style="display:inline-block;margin-top:0.5%;margin-left:1.5%">
      <div class="price">{{Math.round(currency.price_change * 100)/100}}$</div>
    </div>
    <div style="display:inline-block;margin-top:0.5%;margin-left:1%">
      <div class="price">({{Math.round(currency.price_change_pct * 10000) / 100 + "%)"}}</div>
    </div>
    <div>
      <CryptoDetails :currency=currency />
    </div>
    <div style="display:inline-block;vertical-align:top;margin-left:54%;margin-top:-13%;">
      <CryptoChart :currency_history=currency_history />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import CryptoDetails from '/src/components/CryptoDetails.vue';
import CryptoChart from '/src/components/CryptoChart.vue';

export default {
  components: {
    CryptoDetails,
    CryptoChart,
  },
  data() {
    return {
      currency: {
        circulating_supply: "",
        code: "",
        first_order_book: "",
        first_trade: "",
        high: "",
        high_timestamp: "",
        logo_url: "",
        market_cap: "",
        market_cap_dominance: "",
        max_supply: "",
        name: "",
        num_exchanges: "",
        num_pairs: "",
        num_pairs_unmapped: "",
        price: "",
        price_change: "",
        price_change_pct: "",
        price_timestamp: "",
        status: "",
        volume: "",
      },
      currency_history: [],    //lista z danymi historycznymi
    };
  },
  methods: {
    getCurrency(currencyId) {    //metoda wysyła request po walutę do wyświetlenia
      const url =
        "http://localhost:5000/CryptoCurrency/get_cryptocurrencies_by_code";
      const data = {
        meta: {
          method: "get_cryptocurrencies_by_code",
          args: {
            currencies_list: currencyId,
          },
        },
      };

      axios.post(url, data).then(
        (response) => {
          if (response.data.meta.result.result.length > 0) {
            let curr = response.data.meta.result.result[0].attributes;
            console.log(curr);
            this.currency = curr;
          }
        },
        (error) => {
          console.log(error);
        }
      );
    },

    getCurrencyHistory(currencyId) {     //metoda wysyła request po historię waluty
      const url =
        "http://localhost:5000/CryptoCurrency/get_cryptocurrency_history";
      const data = {
        meta: {
          method: "get_cryptocurrency_history",
          args: {
            cryptocurrency_code: currencyId,
          },
        },
      };

      axios.post(url, data).then(
        (response) => {
          if (response.data.meta.result.result.length > 0) {
            let curr = response.data.meta.result.result;
            this.currency_history = curr;
          }
        },
        (error) => {
          console.log(error);
        }
      );
    },
  },

  mounted() {
    this.getCurrency(this.$route.params.code);
    this.getCurrencyHistory(this.$route.params.code);
  },
};
</script>

<style>

.price {
    padding-top: 2%;
    font-size: 200%;
  }

</style>
