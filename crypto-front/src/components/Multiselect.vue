<template>
<div style="margin-left:20%;margin-bottom:2%;">
  <label class="typo__label">Select watched cryptocurrencies:</label>
  <multiselect
   id='mselect'
   @close="onClose"
   @select="onSelect"
   @remove="onRemove"
   style="width: 20%"
    v-model="baths" 
    :options="options" 
    :multiple="true" 
    :close-on-select="false" 
    :clear-on-select="false" 
    :preserve-search="true" 
    placeholder="Pick some" 
    label="name" 
    track-by="name" 
    :allow-empty="true">
    <template slot="selection" slot-scope="{ values, isOpen }">
        <span class="multiselect__single" v-if="values.length &amp;&amp; !isOpen">
            {{ values.length }} options selected
            </span>
    </template>

    <template slot="option" slot-scope="props"><img :width=30 :height=30 class="option__image" :src="props.option.img" alt="No Man’s Sky">
      <div class="option__desc"><span class="option__title">{{ props.option.name }}</span></div>
    </template>
    
  </multiselect>
</div>
</template>

<script>
import Multiselect from 'vue-multiselect'

export default {
  components: {
    Multiselect
  },
  props: {
      baths: Array,
  },
  data () {
    return {
    options: [
        { name: 'Bitcoin', code: 'BTC', img: "https://s3.us-east-2.amazonaws.com/nomics-api/static/images/currencies/btc.svg"},
        { name: 'Etherum', code: 'ETH', img: "https://s3.us-east-2.amazonaws.com/nomics-api/static/images/currencies/eth.svg"},
        { name: 'HEX', code: 'HEX', img: "https://s3.us-east-2.amazonaws.com/nomics-api/static/images/currencies/HEX.png"},
        { name: 'Polygon', code: 'MATIC', img: "https://s3.us-east-2.amazonaws.com/nomics-api/static/images/currencies/matic.png"},
        { name: 'Dogecoin', code: 'DOGE', img: "https://s3.us-east-2.amazonaws.com/nomics-api/static/images/currencies/doge.svg"},
        { name: 'Tron', code: 'TRX', img: "https://s3.us-east-2.amazonaws.com/nomics-api/static/images/currencies/trx.svg"},
        { name: 'Binance Coin', code: 'BNB', img: "https://s3.us-east-2.amazonaws.com/nomics-api/static/images/currencies/bnb.svg"},
        { name: 'Ripple', code: 'XRP', img: "https://s3.us-east-2.amazonaws.com/nomics-api/static/images/currencies/XRP.svg"},
        { name: 'Cardano', code: 'ADA', img: "https://s3.us-east-2.amazonaws.com/nomics-api/static/images/currencies/ada.svg"},
        { name: 'Tether', code: 'USDT', img: "https://s3.us-east-2.amazonaws.com/nomics-api/static/images/currencies/usdt.svg"},
        { name: 'Polkadot', code: 'DOT', img: "https://s3.us-east-2.amazonaws.com/nomics-api/static/images/currencies/DOT.svg"},
        { name: 'Dfinity', code: 'ICP', img: "https://s3.us-east-2.amazonaws.com/nomics-api/static/images/currencies/ICP.jpg"},
        { name: 'Bitcoin Cash', code: 'BCH', img: "https://s3.us-east-2.amazonaws.com/nomics-api/static/images/currencies/BCH.svg"},
        { name: 'Litecoin', code: 'LTC', img: "https://s3.us-east-2.amazonaws.com/nomics-api/static/images/currencies/ltc.svg"},
        { name: 'ChainLink', code: 'LINK', img: "https://s3.us-east-2.amazonaws.com/nomics-api/static/images/currencies/LINK.jpg"},
        { name: 'Shiba Inu', code: 'SHIB', img: "https://s3.us-east-2.amazonaws.com/nomics-api/static/images/currencies/SHIB.png"},
        { name: 'VeChain Thor', code: 'VET', img: "https://s3.us-east-2.amazonaws.com/nomics-api/static/images/currencies/vet.png"},
        { name: 'Aave', code: 'AAVE', img: "https://s3.us-east-2.amazonaws.com/nomics-api/static/images/currencies/AAVE.jpg"},
        { name: 'Monero', code: 'XMR', img: "https://s3.us-east-2.amazonaws.com/nomics-api/static/images/currencies/xmr.svg"},
        { name: 'Neo', code: 'NEO', img: "https://s3.us-east-2.amazonaws.com/nomics-api/static/images/currencies/neo.svg"},
        { name: 'Luna', code: 'LUNA', img: "https://s3.us-east-2.amazonaws.com/nomics-api/static/images/currencies/LUNA.jpg"}
    ],
    selected: []
    }
  },
  methods: {
      onClose() {
        if (this.selected != this.baths) {
          this.selected = [...this.baths];
          this.$emit("close", this.baths);
        }
      },

      onSelect(value) {
          this.selected.push(value)
      },

      onRemove(value) {
          let n = [];
          let index = this.selected.indexOf(value);
          for (let i = 0; i < this.selected.length; i++) {
              if (i != index) {
                  n.push(this.selected[i])
              }
          }
          this.selected = n;
      }
  },
  mounted() {
      this.selected = [...this.baths]
    }
}

</script>

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
