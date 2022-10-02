import axios from 'axios'

export default {
    async searchMoonquakes (payload) {
        let query = Object.keys(payload)
            .filter(q => payload[q] !== null)
            .map(q => `${q}=${encodeURIComponent(payload[q])}`)
            .join('&')
        return await axios.get(`moonquakes/show?${query}`)
    }
}