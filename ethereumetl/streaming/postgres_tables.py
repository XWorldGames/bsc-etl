#  MIT License
#
#  Copyright (c) 2020 Evgeny Medvedev, evge.medvedev@gmail.com
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

from sqlalchemy import Table, Column, Integer, BigInteger, LargeBinary, String, Numeric, MetaData, TIMESTAMP, Boolean

metadata = MetaData()

# SQL schema is here https://github.com/blockchain-etl/ethereum-etl-postgres/tree/master/schema

BLOCKS = Table(
    'blocks', metadata,
    Column('timestamp', TIMESTAMP),
    Column('number', BigInteger),
    Column('hash', LargeBinary, primary_key=True),
    Column('parent_hash', LargeBinary),
    Column('nonce', LargeBinary),
    Column('sha3_uncles', LargeBinary),
    Column('logs_bloom', LargeBinary),
    Column('transactions_root', LargeBinary),
    Column('state_root', LargeBinary),
    Column('receipts_root', LargeBinary),
    Column('miner', LargeBinary),
    Column('difficulty', Numeric(38)),
    Column('total_difficulty', Numeric(38)),
    Column('size', BigInteger),
    Column('extra_data', LargeBinary),
    Column('gas_limit', BigInteger),
    Column('gas_used', BigInteger),
    Column('transaction_count', BigInteger),
    Column('base_fee_per_gas', BigInteger),
)

TRANSACTIONS = Table(
    'transactions', metadata,
    Column('hash', LargeBinary, primary_key=True),
    Column('nonce', BigInteger),
    Column('transaction_index', BigInteger),
    Column('from_address', LargeBinary),
    Column('to_address', LargeBinary),
    Column('value', Numeric(38)),
    Column('gas', BigInteger),
    Column('gas_price', BigInteger),
    Column('input', LargeBinary),
    Column('receipt_cumulative_gas_used', BigInteger),
    Column('receipt_gas_used', BigInteger),
    Column('receipt_contract_address', LargeBinary),
    Column('receipt_root', LargeBinary),
    Column('receipt_status', BigInteger),
    Column('block_timestamp', TIMESTAMP),
    Column('block_number', BigInteger),
    Column('block_hash', LargeBinary),
    Column('max_fee_per_gas', BigInteger),
    Column('max_priority_fee_per_gas', BigInteger),
    Column('transaction_type', BigInteger),
    Column('receipt_effective_gas_price', BigInteger),
)

LOGS = Table(
    'logs', metadata,
    Column('log_index', BigInteger, primary_key=True),
    Column('transaction_hash', LargeBinary, primary_key=True),
    Column('transaction_index', BigInteger),
    Column('address', LargeBinary),
    Column('data', LargeBinary),
    Column('topic0', LargeBinary),
    Column('topic1', LargeBinary),
    Column('topic2', LargeBinary),
    Column('topic3', LargeBinary),
    Column('block_timestamp', TIMESTAMP),
    Column('block_number', BigInteger),
    Column('block_hash', LargeBinary),
)

TOKEN_TRANSFERS = Table(
    'token_transfers', metadata,
    Column('token_address', LargeBinary),
    Column('from_address', LargeBinary),
    Column('to_address', LargeBinary),
    Column('value', Numeric(78)),
    Column('transaction_hash', LargeBinary, primary_key=True),
    Column('log_index', BigInteger, primary_key=True),
    Column('block_timestamp', TIMESTAMP),
    Column('block_number', BigInteger),
    Column('block_hash', LargeBinary),
)

TRACES = Table(
    'traces', metadata,
    Column('transaction_hash', LargeBinary),
    Column('transaction_index', BigInteger),
    Column('from_address', LargeBinary),
    Column('to_address', LargeBinary),
    Column('value', Numeric(38)),
    Column('input', LargeBinary),
    Column('output', LargeBinary),
    Column('trace_type', String),
    Column('call_type', String),
    Column('reward_type', String),
    Column('gas', BigInteger),
    Column('gas_used', BigInteger),
    Column('subtraces', BigInteger),
    Column('trace_address', String),
    Column('error', String),
    Column('status', Integer),
    Column('block_timestamp', TIMESTAMP),
    Column('block_number', BigInteger),
    Column('block_hash', LargeBinary),
    Column('trace_id', String, primary_key=True),
)

TOKENS = Table(
    'tokens', metadata,
    Column('address', LargeBinary, primary_key=True),
    Column('name', String),
    Column('symbol', String),
    Column('decimals', Integer),
    Column('total_supply', Numeric(78)),
    Column('function_sighashes', LargeBinary),
)

CONTRACTS = Table(
    'contracts', metadata,
    Column('address', LargeBinary, primary_key=True),
    Column('bytecode', LargeBinary),
    Column('function_sighashes', LargeBinary),
    Column('is_erc20', Boolean),
    Column('is_erc721', Boolean),
    Column('block_number', BigInteger),
)
