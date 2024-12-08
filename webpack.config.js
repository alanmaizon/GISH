const path = require('path');

module.exports = {
    entry: './static/js/script.js', // Your main JS file
    output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname, 'static/dist'), // Bundled output
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['@babel/preset-env'], // Use Babel for ES6+ support
                    },
                },
            },
        ],
    },
    mode: 'development', // Change to 'production' for optimized builds
    devtool: 'source-map', // Enable source maps for easier debugging
};
