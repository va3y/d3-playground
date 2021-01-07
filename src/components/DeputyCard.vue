<template>
  <div>
{{ name }}
<br>
{{ faction }}
<br>
{{ isCurrent==true ? 'Текущий депутат\n':'' }}
<br>
<br>

  </div>
</template>

<script>
export default {
  name: 'DeputyCard',
  props: ['depId','name','isCurrent','faction']
}
</script>

<style lang="scss" scoped>

</style>