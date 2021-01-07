<template>
  <div>
    <Chart />
    <label for="isCurrent">Партия</label>
    <select name="faction" v-model="selectedFaction">
      <option value="72100024">Единая Россия</option>
      <option value="72100027">Справедливая Россия</option>
      <option value="72100005">ЛДПР</option>
      <option value="72100004">КПРФ</option>
      <option value="all">Не важно</option>
    </select>

    <label for="isCurrent">Текущий депутат</label>
    <select name="isCurrent" v-model="isCurrentSwitch">
      <option :value="true">Да</option>
      <option :value="false">Нет</option>
      <option value="all">Не важно</option>
    </select>
    Найдено депутатов: {{ getDepCount }}

    <DeputyCard v-for="dep in isShown" :key="dep.id"
      :name=dep.name :depId=dep.id :isCurrent=dep.isCurrent
      :faction=getFactions(dep.factions) />
  </div>
</template>

<script>
import * as d3 from "d3";
import DeputyCard from "./DeputyCard.vue"
import Chart from "./Chart.vue"
export default {
  
  name: "Selector",
  components: {
    DeputyCard,
    Chart
  },
  data() {
    return {
      data: null,
      isCurrentSwitch: "all",
      selectedFaction: 'all'
    };
  },
  created() {
    this.chart();
  },
  methods: {
    async chart() {
      const data = await d3.json("./deputies.json");
      this.data = data;
    },
    getFactions(factions) {
      let faction = "";
      try {
        faction = factions[0].name;
      } catch (error) {
        faction = "Член Совета Федерации";
      }
      return faction;
    },
  },
  computed: {
    isShown: function () {
      try {
        const shownData = this.data.filter((dep) => {
          let isCurr = true;
          if (this.isCurrentSwitch != "all") {
            isCurr = dep.isCurrent == this.isCurrentSwitch;
          }
          let faction = true;
          if (this.selectedFaction != "all") {
            try {
              faction = dep.factions[dep.factions.length-1].id == this.selectedFaction;
            } catch (error) {
              faction = false
            }
          }

          return isCurr && faction;
        });

        return shownData;
      } catch (error) {
        console.log("not yet");
        return "not yet";
      }
    },
    getDepCount: function () {
      try {
        return this.isShown.length;
      } catch (error) {
        return "not yet";
      }
    },
  },
};
</script>

<style lang="scss" scoped>
</style>