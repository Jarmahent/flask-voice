<template>
  <div>
    <h5 style="color: green !important;" v-if="showBugSubmitted">Your bug was submitted!</h5>
    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
      <b-form-group
        id="input-group-1"
        label="Email address:"
        label-for="input-1"
        description="Incase we have more questions"
      >
        <b-form-input
          id="input-1"
          v-model="form.email"
          type="email"
          required
          placeholder="Enter email"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Your Name:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="form.name"
          required
          placeholder="Enter name"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-3" label="Severity:" label-for="input-3">
        <b-form-select
          id="input-3"
          v-model="form.severity"
          :options="severity"
          required
        ></b-form-select>
      </b-form-group>
      <b-form-group id="input-group-3" label="Describe the issue:" label-for="input-3">
        <b-form-textarea
          id="input-4"
          v-model="form.body"
          required
          >
        </b-form-textarea>
      </b-form-group>

      <b-button type="submit" variant="primary">Submit</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
    </b-form>
  </div>
</template>

<script>
import request from "superagent";

  export default {
    data() {
      return {
        form: {
          email: '',
          name: '',
          severity: null,
          body: ''
        },
        severity: [{ text: 'Select One', value: null }, 'Enhancement', 'Normal', 'High', 'Critical'],
        show: true,
        showBugSubmitted: false
      }
    },
    methods: {
      onSubmit(evt) {
        evt.preventDefault()
        request
        .post('/api/submitbug')
        .send({
          form: this.form
        })
        .then(res =>{
          this.onReset();
          this.showBugSubmitted = true
        })
      },
      onReset(evt) {
        // Reset our form values
        this.form.email = ''
        this.form.name = ''
        this.form.body = ''
        this.form.severity = null
        this.form.checked = []
        // Trick to reset/clear native browser form validation state
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
      }
    }
  }
</script>
