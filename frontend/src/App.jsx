import React, { useState } from 'react';
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';
import './App.css';
import DateTimePicker from './components/DateTimePicker';

const App = () => {
  const [startDate, setStartDate] = useState(null);
  const [endDate, setEndDate] = useState(null);
  const [responseData, setResponseData] = useState(null);
  const [error, setError] = useState(false);

  const handleStartDateChange = (date) => {
    setStartDate(date);
  };

  const handleEndDateChange = (date) => {
    setEndDate(date);
  };

  const handleButtonClick = () => {
    if (!startDate || !endDate) {
      alert('Please select both start and end dates.');
      return;
    }

    // Construct the API URL with start and end dates
    const apiUrl = `http://localhost/status_count?start=${startDate.toISOString()}&end=${endDate.toISOString()}`;

    // Perform your fetch or Axios call here
    fetch(apiUrl)
      .then(response => response.json())
      .then(data => {
        setResponseData(data);
        setError(false);
        console.log('Fetched data:', data);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
        setError(true);
      });
  };

  return (
    <div>
      <h1>Enter Time range</h1>
      <DateTimePicker heading="Start time" selected={startDate} onChange={handleStartDateChange}/>
      <DateTimePicker heading="End time" selected={endDate} onChange={handleEndDateChange}/>
      <button style={{marginTop:"40px"}} onClick={handleButtonClick}>Fetch Data</button>
      {error ?
        <div className="error">
          <p>An error occurred while fetching data.</p>
        </div>
        : <></>
      }
      <div className="count">
        <h1>{responseData ? responseData.count : 0}</h1>
        <p>Count</p>
      </div>
    </div>
  );
};

export default App;
