import React from 'react';
import {QueryClient, QueryClientProvider, useQuery} from 'react-query'

const queryClient = new QueryClient()

const getProducts = async () => {
    const response = await fetch('http://192.168.0.200:8001/api/products')
    return response.json()
}

function App() {
    return (
        <QueryClientProvider client={queryClient}>
            <ProductList/>
        </QueryClientProvider>
    )
}

function ProductList() {
    const {status, data, isFetching, error} = useQuery('products', getProducts)

    if (status === 'loading'){
        return <div>loading..</div> //loading state
    }
    if (status === 'error') {
        return <div>{error.message}</div> //error state
    }

    return (
        <div>
            { data && <ul> {
                data.slice(0,10).map(d => <li key={`post-${d.id}`}>{d.title} <img src={d.image}/> /></li>)
                }</ul> }
            { isFetching && <p>updating...</p> }
        </div>
    )
}

export default App
