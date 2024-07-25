<template>
  <div id="currencies-table">
    <Multiselect v-if="$auth.isAuthenticated" :baths=currencies_list @close="onMenuClosed" />
    <CryptoTable :items=items />
    <div style="min-height: 300px">

    </div>
  </div>
</template>

<script>

import CryptoTable from '/src/components/CryptoTable.vue'
import axios from 'axios'
import Multiselect from '../components/Multiselect.vue';

export default {
  name: "Home",
  components: {
    CryptoTable,
    Multiselect,
  },
  data() {
    return {
      items: [],
      resultsData: [],
      currencies_list: [],
      xd: null,    
    }
  },
  methods: {
    async getCurrencies() {
      console.log(this.currencies_list.map(x => x.code).join(','));
      this.items = []
      this.resultsData = []
      const url =
        "http://localhost:5000/CryptoCurrency/get_cryptocurrencies_by_code";
      const data = {
        meta: {
          method: "get_cryptocurrencies_by_code",
          args: {
            currencies_list: this.currencies_list.map(x => x.code).join(','),
          },
        },
      };
      axios.post(url, data).then(
        (response) => {
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
    onMenuClosed(value) {
    //tutaj trzeba dodać to PATCH żeby userowi ustawić taką listę cryptosów
      let n = [...value];
      this.currencies_list = n;
      this.getCurrencies();
    }
  },

  mounted() {
    
    var options = {
      method: 'POST',
      url: 'https://' + process.env.VUE_APP_DOMAIN + '/oauth/token',
      headers: {'content-type': 'application/x-www-form-urlencoded'},
      data: {
        grant_type: 'client_credentials',
        client_id: process.env.VUE_APP_CLIENT_ID,
        client_secret: process.env.VUE_APP_CLIENT_SECRET,
        audience: process.env.VUE_APP_AUDIENCE
      }
    };
    
    console.log('https://' + process.env.VUE_APP_DOMAIN + '/oauth/token');
    
    axios.request(options).then(function (response) {
      this.xd = response.data;
    }).catch(function (error) {
      console.error(error);
    });

    console.log(this.xd)

    if (Object.prototype.hasOwnProperty.call(this.$auth, 'currencies_list')) {
      this.currencies_list = this.$auth.currencies_list;
    } else {
      this.currencies_list = [
        { name: 'Bitcoin', code: 'BTC'},
        { name: 'Etherum', code: 'ETH'},
        { name: 'HEX', code: 'HEX'},
        { name: 'Polygon', code: 'MATIC'},
        { name: 'Dogecoin', code: 'DOGE'},
        { name: 'Tron', code: 'TRX'},
        { name: 'Binance Coin', code: 'BNB'},
        { name: 'Ripple', code: 'XRP'},
        { name: 'Cardano', code: 'ADA'},
        { name: 'Tether', code: 'USDT'},
        { name: 'Polkadot', code: 'DOT'},
        { name: 'Dfinity', code: 'ICP'},
        { name: 'Bitcoin Cash', code: 'BCH'},
        { name: 'Litecoin', code: 'LTC'},
        { name: 'ChainLink', code: 'LINK'},
        { name: 'Shiba Inu', code: 'SHIB'},
        { name: 'VeChain Thor', code: 'VET'},
        { name: 'Aave', code: 'AAVE'},
        { name: 'Monero', code: 'XMR'},
        { name: 'Neo', code: 'NEO'},
        { name: 'Luna', code: 'LUNA'} ]
    }
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