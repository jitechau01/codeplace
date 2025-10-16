CREATE TABLE regions (
  region_id NUMBER,
  region_name VARCHAR2(25)
);

CREATE TABLE countries (
  country_id CHAR(2),
  country_name VARCHAR2(40),
  region_id NUMBER
);

CREATE TABLE locations (
  location_id    NUMBER(4),
  street_address VARCHAR2(40),
  postal_code    VARCHAR2(12),
  city       VARCHAR2(30),
  state_province VARCHAR2(25),
  country_id     CHAR(2)
);

CREATE TABLE departments (
  department_id    NUMBER(4),
  department_name  VARCHAR2(30),
  manager_id       NUMBER(6),
  location_id      NUMBER(4)
);

CREATE TABLE jobs (
  job_id         VARCHAR2(10),
  job_title      VARCHAR2(35),
  min_salary     NUMBER(6),
  max_salary     NUMBER(6)
);

CREATE TABLE employees (
  employee_id    NUMBER(6),
  first_name     VARCHAR2(20),
  last_name      VARCHAR2(25),
  email          VARCHAR2(25),
  phone_number   VARCHAR2(20),
  hire_date      DATE,
  job_id         VARCHAR2(10),
  salary         NUMBER(8,2),
  commission_pct NUMBER(2,2),
  manager_id     NUMBER(6),
  department_id  NUMBER(4)
);

CREATE TABLE job_history (
  employee_id   NUMBER(6),
  start_date    DATE,
  end_date      DATE,
  job_id        VARCHAR2(10),
  department_id NUMBER(4)
);
