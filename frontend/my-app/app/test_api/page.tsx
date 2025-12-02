"use client";

import React, { useEffect, useState } from 'react';
import { json } from 'stream/consumers';

interface StockData {
    open: number,
    high: number,
    low: number,
    close: number, 
    volume: number,
}

interface StatCardProps {
    title: string;
    value: number;
}

const StatCard = ({ title, value }: StatCardProps) => {
    return (
        <div className="bg-white p-6 rounded-xl shadow-lg border-l-4 border-gray-300">
            <h3 className="text-md font-medium text-gray-500 mb-1">{title}</h3>
            <p className="text-3xl font-extrabold text-gray-900">{value}</p>
        </div>
    );
};

const StatsPage = () => {
    {/* User Input/Search Bar */}
    const [searchQuery, setSearchQuery] = useState('');

    {/* Fetching data */}
    const [stockData, setStockData] = useState<StockData | null>(null);

    {/* Loading/Error state */}
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);

    {/* API Fetching Logic */}
    useEffect(() => {
        // If search bar empty don't fetch
        if (!searchQuery) {
            setStockData(null);
            setError(null);
            return;
        }

        const fetchData = async () => {
            setIsLoading(true);
            setError(null);

            // Dependent on local host
            const BASE_URL = 'http:localhost:3000'; 

            const Ticker = searchQuery.toUpperCase();           // user input
            const Fields = "open, high, low, close, volume";    // data we want
            const Conditions = `ticker = '{Ticker}''`;          // find data using ticker
            
            // Initiate request for data
            const url = `${BASE_URL}/extract/${Ticker}/${Fields}/${Conditions}/data`;

            console.log("Fetching data from:", url);

            {/* Fetch and Response handling */}
            try {
                // API CALL
                const response = await fetch(url);

                if (!response.ok) {
                    // Error handling
                    throw new Error(`Server responded with status: ${response.status}`);
                }
                
                const jsonResponse = await response.json();
                // Proccess the response
                if (jsonResponse.length > 0) {
                    setStockData(jsonResponse[0] as StockData);
                } 
                else {
                    setError(`No data found for for ticker: ${Ticker}`);
                    setStockData(null);
                }

            } catch (err: any) {
                console.error("Fetch error:", err);
                setError(`Failed to fetch data: ${err.message}`);
                setStockData(null);
            } finally {
                setIsLoading(false); // stop loading whether work or doesn't
            }
        };
    // run fetch
    fetchData();
    }, [searchQuery]); // dependent on search, rerun whenever search changes

    // set default to 0 if no data is loaded yet
    const displayData = stockData || {open: 0, high: 0, low: 0, close: 0, volume: 0};

    return (
        <div className="bg-white min-h-screen flex flex-col items-center p-8 font-inter">
            <h2 className="text-3xl font-bold text-gray-900 mb-6">API Testing</h2>

            {/* Search Bar */}
            <input 
                type="text" 
                placeholder="Enter company"
                className="w-full max-w-6xl p-3 mb-4 border border-gray-300 rounded-lg shadow-sm 
                focus:ring-blue-500 focus:border-blue-500 transition-colors placeholder-gray-700
                placeholder:italic"

                value={searchQuery}
                onChange={(character) => setSearchQuery(character.target.value)}    
            />

            {/* Conditional Loading/Error msgs */}
            {isLoading && (
                <p className="text-xl text-blue-600 mb-6 font-medium animate-pulse">
                    <span role="img" aria-label="loading">⏳</span> Loading data for **{searchQuery}**...
                </p> 
            )}
            {error && (
                <div className="bg-red-100 border-l-4 border-red-500 text-red-700 p-4 w-full max-w-6xl mb-6" role="alert">
                    <p className="font-bold">Fetch Error</p>
                    <p>{error}</p>
                </div>
            )}

            {/* Stat cards */}
            <div className="grid grid-cols-2 md:grid-cols-5 gap-6 max-w-6xl w-full">
            <StatCard title="Open" value={displayData.open} />
            <StatCard title="High" value={displayData.high} />
            <StatCard title="Low" value={displayData.low} />
            <StatCard title="Close" value={displayData.close} />
            <StatCard title="Volume" value={displayData.volume} />
            </div>
        </div>
    )
}

export default StatsPage;