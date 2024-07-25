<template>
  <div>
    <div style="display:inline-block;vertical-align:top;margin-left:20%;margin-top:5%;font-size:95%">
      <p><strong>Circulating supply:</strong> {{currency.circulating_supply}} </p>
      <p><strong>First order book:</strong> {{currency.first_order_book}} </p>
      <p><strong>First trade:</strong> {{currency.first_trade}} </p>
      <p><strong>Highest value:</strong> {{currency.high}}$</p>
      <p><strong>Highest value time:</strong> {{currency.high_timestamp}} </p>
      <p><strong>Market cap:</strong> {{currency.market_cap}} </p>
    </div>
    <div style="display:inline-block;vertical-align:top;margin-left:2%;margin-top:5%;font-size:95%">
      <p><strong>Max supply:</strong> {{currency.max_supply}} </p>
      <p><strong>Number of exchanges:</strong> {{currency.num_exchanges}} </p>
      <p><strong>Number of pairs:</strong> {{currency.num_pairs}} </p>
      <p><strong>Number of pairs (u):</strong> {{currency.num_pairs_unmapped}} </p>
      <p><strong>Status:</strong> {{currency.status}} </p>
      <p><strong>Volume:</strong> {{currency.volume}} </p>
    </div>
  </div>
</template>

<script>
export default {
  name: "CryptoDetails",
  props: {
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
  },

};
</script>

<style scoped>

</style>