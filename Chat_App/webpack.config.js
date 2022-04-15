const path = require("path");
const webpack = require("webpack");
module.exports = {
  entry: {
    main:path.resolve(__dirname, 'src'),
  },
  output: {
    path:path.resolve(__dirname, 'static/Chat_App_frontend'),
    filename:"main.js"
  },
  resolve: {

    modules: ["node_modules",path.resolve(__dirname, "src/")],
    // directories where to look for modules (in order)
    extensions: [".js", ".json", ".jsx", ".css"]
  },
  module:{
    
    rules: [
      {
        test: /\.jsx|.js$/, 
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        },
      },
      {
        test:/\.css$/,
        exclude:/node_modules/,
        use:["style-loader","css-loader"]
      }
    ],
},
plugins:[
  new webpack.DefinePlugin({
    "process.env":{
      NODE_ENV: JSON.stringify("development")
    }
  })
]

};

