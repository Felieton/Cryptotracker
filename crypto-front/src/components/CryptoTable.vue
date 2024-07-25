<template>
  <div>
    <div>
      <b-table
        class="table"
        striped
        hover
        :items="items"
        @row-clicked="currencyDetails"
      >
        <template #cell(image)="data">
          <img :src="data.value" :width="40" :height="40" />
        </template>
      </b-table>
    </div>
  </div>
</template>

<script>
export default {
  name: "CryptoTable",
  props: {
    msg: String,
    items: Array,
  },
  methods: {
    currencyDetails(crypto) {
      this.$router.push({ path: "/crypto/"+crypto.code});
    },
  },
  data() {
    return {
      resultsData: [],
      fields: [{}],
    };
  },
  mounted() {
    this.getCurrencies();
  },
};
</script>

<style scoped>
.table {
  margin-top: 3%;
  max-width: 1000px;
  margin: auto;
}
</style>