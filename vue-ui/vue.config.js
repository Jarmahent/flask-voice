module.exports = {
  outputDir: "../app/templates/index",
  runtimeCompiler: true,
  publicPath: process.env.NODE_ENV === 'production'
  ? '/index'
  : '/'
};