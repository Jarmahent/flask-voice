<template>
  <div>
    <a>
      <div class="row bigListArticles">
        <div class="col-10">
          <img :src="articleThumbnail" class="img-fluid" />
          <h5>{{articleTitle}}</h5>
          <p v-if="articlePreview">{{cutBody}}</p>
          <p v-else>{{articleBody}}</p>
          <b-button @click="expandArticle" variant="outline-primary">{{expandOrShrink}}</b-button>
          <h5>{{articleUrl}}</h5>
        </div>
        <div class="col-2">
          <a href="#" @click="playArticle" v-if="!loadingArticleMedia">
           <img v-if="media_paused" src="../assets/play_icon.png" class="img-fluid platBtn" />
           <img v-else src="../assets/pause-icon.png" class="img-fluid platBtn" />
          </a>
          <div v-else>
            <b-spinner variant="secondary"></b-spinner>
          </div>
        </div>
      </div>
    </a>
  </div>
</template>
<script>
import request from 'superagent'

export default {
  name: "ArticleSnippet",
  props: ["articleTitle", "articleBody", "articleId", "articleThumbnail"],
  created(){
    var re = /(.{0,300})(\s+|$)/g;
    var unJoined = re.exec(this.articleBody.replace(/(\r\n|\n|\r)/gm, ''));
    this.cutBody = unJoined.join() + '...';
  },
  data(){
    return {
      cutBody: null,
      loadingArticleMedia: false,
      articlePreview: true,
      expandOrShrink: 'Expand',
      articleLoaded: false,
      media_paused: true,
      audio: null,
      articleUrl: null
    }
  },
  methods: {
    playArticle(e){
      e.preventDefault()
      if(this.articleLoaded){
        if(this.media_paused){
          this.media_paused = false;
          this.audio.play()
        }else{
          this.media_paused = true;
          this.audio.pause();
        }
      }else{
        this.loadingArticleMedia = true;
        request
        .get(`/api/fetch?id=${this.articleId}`)
        .then((response) =>{
          this.loadingArticleMedia = false;
          this.articleLoaded = true;
          this.audio = new Audio(response.body.media);
          this.media_paused = false;
          this.audio.play();
        });
      }

    },
    expandArticle(e){
      this.articlePreview = !this.articlePreview;
      if(this.articlePreview){
        this.expandOrShrink = 'Expand'
      }else{
        this.expandOrShrink = 'Shrink'
      }
    }
  }
};
</script>
