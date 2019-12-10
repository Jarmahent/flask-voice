<template >
  <div>
    <b-modal ref="submit-bug-modal" hide-footer title="Report a Bug">
      <ReportBugModal />
    </b-modal>
    <div class="container-fluid">
      <div class="row header">
        <div class="container">
          <div class="row">
          <div class="col">
            <img src="../assets/articlevoice.png" class="img-fluid logo" />
          </div>
          <div class="col pull-right text-right">
            <a href="#" @click="showReportBug">Report a bug</a>
          </div>
          </div>
        </div>
      </div>
      <!--row-->
      <div class="row jumboHomeHero">
        <div class="jumbotron jumbotron-fluid">
          <div class="container">
            <div class="row">
            <div class="col">
              <h1 class="display-4">Save your eyes&mdash;listen to the news.</h1>
              <p
                class="lead"
              >Convert text articles into voice, this app is made for people who find it hard to focus on an article and would prefer to listen to it in the background!</p>
            </div>
            <div class="col"></div>
            </div>
            <div class="row">
            <div class="col-sm-12">
                <b-form @submit.stop.prevent="convertArticle">
                <b-form-input v-model="url" placeholder="Article URL..."></b-form-input>
                <b-button
                  class="mt-2 mr-2 convertBtn"
                  variant="outline-secondary"
                  @click="convertArticle"
                  v-if="!loading"
                >Convert!</b-button>
                <a :href="href" download v-if="requestSuccess">Download Zip file</a>
                <h4 style="color: red;" v-if="invalidUrl">The url needs to be valid or https</h4>
              </b-form>
              <b-spinner v-if="loading" class="m-3"></b-spinner>
              <audio :src="media_source" v-if="requestSuccess" controls />
            </div>
            </div>
          </div>
        </div>
        <!--jumbotron-->
      </div>
      <!--row-->
      <div id="theDonateBar" class="row">
        <div class="container">
          <div class="row">

          <div class="col text-right justASpeal"><strong>Your donations keep us going.</strong> <br />10%&mdash;this months charity.</div>
          <div class="col text-left"><img src="https://connect4water.files.wordpress.com/2014/03/charity_water.png" class="img-fluid" /></div>
          <div class="col">
              <b-button
                  class="mt-2 mr-2"
                  variant="outline-secondary">
                Donate!
              </b-button>
            </div>
          </div>
        </div>
      </div>
      <!--row-->
    </div>
    <b-card v-if="requestSuccess" class="mt-3">
      <h2>{{article_title}}</h2>
      <b-form-textarea
        id="textarea-plaintext"
        plaintext
        :value="article_text"
        rows="25"
        max-rows="25"
      ></b-form-textarea>
    </b-card>
    <div class="row">
      <div class="container">
        <!--<img src="../assets/chrome_1py0MbPTcn.png" class="img-fluid logo" />-->
      </div>
    </div>
    <!--row-->
    <div id="savedFeed" class="row">
      <div class="container">
        <div class="row">
          <aside class="col-3">
            <p>Filter 3</p>

            <div class="card">
              <article class="card-group-item">
                <header class="card-header">
                  <h6 class="title">Range input</h6>
                </header>
                <div class="filter-content">
                  <div class="card-body">
                    <div class="form-row">
                      <div class="form-group col-md-6">
                        <label>Min</label>
                        <input type="number" class="form-control" id="inputEmail4" placeholder="$0" />
                      </div>
                      <div class="form-group col-md-6 text-right">
                        <label>Max</label>
                        <input type="number" class="form-control" placeholder="$1,0000" />
                      </div>
                    </div>
                  </div>
                  <!-- card-body.// -->
                </div>
              </article>
              <!-- card-group-item.// -->
              <article class="card-group-item">
                <header class="card-header">
                  <h6 class="title">Selection</h6>
                </header>
                <div class="filter-content">
                  <div class="card-body">
                    <div class="custom-control custom-checkbox">
                      <span class="float-right badge badge-light round">52</span>
                      <input type="checkbox" class="custom-control-input" id="Check1" />
                      <label class="custom-control-label" for="Check1">Samsung</label>
                    </div>
                    <!-- form-check.// -->

                    <div class="custom-control custom-checkbox">
                      <span class="float-right badge badge-light round">132</span>
                      <input type="checkbox" class="custom-control-input" id="Check2" />
                      <label class="custom-control-label" for="Check2">Black berry</label>
                    </div>
                    <!-- form-check.// -->

                    <div class="custom-control custom-checkbox">
                      <span class="float-right badge badge-light round">17</span>
                      <input type="checkbox" class="custom-control-input" id="Check3" />
                      <label class="custom-control-label" for="Check3">Samsung</label>
                    </div>
                    <!-- form-check.// -->

                    <div class="custom-control custom-checkbox">
                      <span class="float-right badge badge-light round">7</span>
                      <input type="checkbox" class="custom-control-input" id="Check4" />
                      <label class="custom-control-label" for="Check4">Other Brand</label>
                    </div>
                    <!-- form-check.// -->
                  </div>
                  <!-- card-body.// -->
                </div>
              </article>
              <!-- card-group-item.// -->
            </div>
            <!-- card.// -->
          </aside>
          <!-- col.// -->
          <div class="col-9">
            <h2 v-if="noRecentArticles">No Recent Articles</h2>
            <div v-for="article in recentArticles" v-bind:key="article">
              <ArticleSnippet :articlePath="article"/>
            </div>
          </div>
        </div>
        <!--row-->
      </div>
      <!--container-->
    </div>
    <!--savedFeed-->
  </div>
</template>


<script>
import request from "superagent";
import ArticleSnippet from "./ArticleSnippet";
import AdSection from "./AdSection";
import ReportBugModal from './ReportBug'

export default {
  name: "HomePage",
  components: {
    ArticleSnippet,
    AdSection,
    ReportBugModal
  },
  data() {
    return {
      url: "",
      article_text: "",
      requestSuccess: false,
      loading: false,
      ready: false,
      href: "",
      invalidUrl: false,
      media_source: null,
      recentArticles: null,
      noRecentArticles: false,
      article_title: '',
      csrf: null,
      showReportBugModal: false
    };
  },
  created(){
    this.getRecentArticles();
  },
  methods: {
    convertArticle() {
      if (this.url === "") {
        return null;
      }
      if (!this.validate(this.url)) {
        this.invalidUrl = true;
        return null;
      } else {
        this.loading = true;
        request
          .post("http://127.0.0.1:8000" + "/api/convert")
          .send({
            url: this.url
          })
          .then(res => {
            this.invalidUrl = false;
            this.requestSuccess = true;
            this.loading = false;

            res = JSON.parse(res.text);
            this.media_source = res.article_audio;
            this.article_text = res.article_body;
            this.article_title = res.article_title
            this.href = res.data;
            // const downloadLink = document.createElement("a");
            // const fileName = "voice.zip";

            // downloadLink.href = res.data;
            // downloadLink.download = fileName;
            // downloadLink.setAttribute("type", "hidden"); // make it hidden if needed
            // document.body.appendChild(downloadLink);
            // downloadLink.click();
          });
      }
    },
    getRecentArticles(){
      request
      .get('http://127.0.0.1:8000/api/articles')
      .set('Access-Control-Allow-Origin', "*")
      .then(res => {
        this.recentArticles = res.body.articles
      })
    },
    validate(text) {
      // eslint-disable-next-line
      var reg = /^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$/;
      if (text.match(reg)) {
        return true;
      }
      return false;
    },
    showReportBug(e){
      e.preventDefault();
      this.$refs['submit-bug-modal'].show()
    }
  }
};
</script>
