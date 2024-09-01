import React from 'react';
import jsPDF from 'jspdf';

function PrintModal({ order }) {
  const handlePrint = () => {
    const doc = new jsPDF();
    // 宛名情報をPDFに書き込む
    doc.save('address_label.pdf');
  };

  // モーダル内のUI
  return (
    <div>
      {/* 宛名情報 */}
      <button onClick={handlePrint}>PDFで印刷</button>
    </div>
  );
}