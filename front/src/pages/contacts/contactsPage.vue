<template>
<h1></h1>
</template>

<script>
export default {
  name: "contacts",
  data() {
    return {
      contacts: [],
      contact_removed:'',
    };
  },
  mounted() {
    this.loadData();
  },

};
</script>

<style scoped>
h1 {
  font-style: italic;
}
.contact-item {
  border: 2px solid dodgerblue;
  border-radius: 1em;
  margin: 1em;
}
</style>
