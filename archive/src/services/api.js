import axios from 'axios';

const BASE_URL = 'https://api.thebase.in/1'; // BASE APIのベースURL

export const fetchOrders = async () => {
  const response = await axios.get(`${BASE_URL}/orders`, {
    headers: {
      Authorization: `Bearer ${localStorage.getItem('accessToken')}`
    }
  });
  return response.data.orders;
};