<template>
	<div class="container">
		<QuestionList :isInstructor="isInstructor" />
  </div>
</template>
<script>
/* eslint-disable */
import QuestionList from "../components/QuestionList.vue";
export default {
	name: "InstructorQuestionView",
	components: {
		QuestionList,
	},
	props: {
		isInstructor: Boolean,
		questions: Array,
	},
}
</script>
