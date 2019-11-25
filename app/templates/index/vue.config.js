module.exports = {
  outputDir: "./index",
  runtimeCompiler: true,
  publicPath: process.env.NODE_ENV === 'production'
  ? '/index/index'
  : '/'
};