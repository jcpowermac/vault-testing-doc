path "secret/ansible/*" {
  policy = "write"
}

path "secret/ansible/*" {
  policy = "read"
}

path "auth/token/lookup-self" {
  policy = "read"
}
