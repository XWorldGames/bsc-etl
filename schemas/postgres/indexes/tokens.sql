alter table tokens add constraint tokens_pk primary key (address);

create index tokens_function_sighashes_index on tokens (function_sighashes);
