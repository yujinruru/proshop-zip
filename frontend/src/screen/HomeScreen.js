import React, { useState, useEffect } from "react";
import { Row, Col } from "react-bootstrap";
import products from "../products";
import { useDispatch, useSelector } from "react-redux";
import Product from "../components/Product";
import axios from "axios";
import { listProducts } from "../actions/productAction";
import Loader from "../components/Loader";
import Message from "../components/Message";

function HomeScreen() {
  const dispatch = useDispatch();
  const productList = useSelector((state) => state.productList);
  const { error, loading, products } = productList;

  useEffect(() => {
    dispatch(listProducts());
  }, [dispatch]);

  // const [products, setProducts] = useState([]);

  // useEffect(() => {
  //   async function fetchProducts() {
  //     const { data } = await axios.get(`/api/products/`);
  //     setProducts(data);
  //   }
  //   fetchProducts();
  // }, []);
  return (
    <div>
      <h1>다양한 뽁뽁이 상품들 dd(updated)</h1>
      {loading ? (
        <Loader />
      ) : error ? (
        <Message variant="danger"> {error} </Message>
      ) : (
        <Row>
          {products.map((product) => (
            <Col key={product._id} sm={12} md={6} lg={4} xl={3}>
              <h3>
                <Product product={product} />
              </h3>
            </Col>
          ))}
        </Row>
      )}
    </div>
  );
}

export default HomeScreen;
