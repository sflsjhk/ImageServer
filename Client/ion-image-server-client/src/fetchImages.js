/* eslint-disable no-unused-vars */
/* eslint-disable camelcase */
/* eslint-disable no-undef-init */
/* eslint-disable indent */
/* eslint-disable no-multiple-empty-lines */
/* eslint-disable no-debugger, no-console */
import axios from 'axios'
axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*'

async function fetchImages (first_name, last_name) {
    const requestData = {
        first_name,
        last_name
    }
    const header = {
        'Access-Control-Allow-Origin': '*',
        'Content-type': 'application/json'
     }
    console.log(first_name, last_name)
    let result = undefined
    try {
        const response = await axios.get('http://localhost:5000', requestData, header)
        result = response.data.imageURLs
    } catch (error) {
        console.log(error)
        result = []
    }
    return result
}

export {
    fetchImages
}
