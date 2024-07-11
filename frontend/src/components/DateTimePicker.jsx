import React, { useState } from 'react';
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';
import './DateTimePicker.css';

const DateTimePicker = ({heading, selected, onChange}) => {
  const [startDate, setStartDate] = useState(new Date());

  return (
    <div className="datetime-picker-container">
      <span>{heading}:</span>
      <DatePicker
        selected={selected}
        onChange={onChange}
        showTimeSelect
        timeFormat="HH:mm"
        timeCaption="Time"
        dateFormat="MMMM d, yyyy h:mm aa"
        className="datetime-picker"
      />
    </div>
  );
};

export default DateTimePicker;
