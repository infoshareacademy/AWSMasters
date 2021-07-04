Instalacja oprogramowania STRESS

```
sudo amazon-linux-extras install epel -y
sudo yum install stress -y
```

Wywołanie dużego obciążenia (CPU) na serwerze

```
stress --cpu 1 --timeout 300
```

Wywołanie dużego obciążenia (Memory) na serwerze

```
cat <( </dev/zero head -c 500m) <(sleep 300) | tail
```
