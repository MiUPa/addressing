import React, { useEffect, useState } from 'react';
import { fetchOrders } from '../../src/services/api';
import PrintModal from './PrintModal';

function OrderList() {
  const [orders, setOrders] = useState([]);
  const [selectedOrder, setSelectedOrder] = useState(null);

  useEffect(() => {
    fetchOrders()
      .then(data => setOrders(data))
      .catch(error => console.error('Error fetching orders:', error));
  }, []);

  const handlePrint = () => {
    // PrintModalを開くか、直接印刷処理を行う
  };

  return (
    <div>
      {/* 注文一覧 */}
      {orders.map(order => (
        <div key={order.id}>
          <input type="radio" name="order" value={order.id} onChange={() => setSelectedOrder(order)} />
          {/* 注文の詳細 */}
        </div>
      ))}
      {selectedOrder && <PrintModal order={selectedOrder} />}
      <button onClick={handlePrint}>印刷</button>
    </div>
  );
}